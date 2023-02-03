# import os
from pathlib import Path
from typing import Optional, Dict

import jinja2
from sphinx.environment import BuildEnvironment
from sphinx.errors import SphinxError

from sphinx_ads.logging import get_logger

logger = get_logger(__name__)


class Template:

    def __init__(self, env: BuildEnvironment):
        self._sphinx_env = env
        self._jinja_env = None

    @property
    def _env(self) -> jinja2.Environment:
        def generate():
            base_path = Path(Path(__file__).parent).resolve()   # Path to folder containing default template files
            template_paths = []

            docs_src_dir = Path(self._sphinx_env.app.confdir)   # Path to folder containing custom template files

            if docs_src_dir.is_dir():
                template_paths.append(docs_src_dir)
            template_paths.append(base_path.joinpath("."))

            file_loader = jinja2.FileSystemLoader(template_paths)
            logging_undefined = jinja2.make_logging_undefined(
                logger=logger, base=jinja2.Undefined
            )
            env = jinja2.Environment(
                loader=file_loader,
                undefined=logging_undefined,
                lstrip_blocks=True,
                trim_blocks=True,
                autoescape=True,
            )

            env.globals["advertisement"] = self.advertisement
            return env

        if not self._jinja_env:
            self._jinja_env = generate()
        return self._jinja_env

    def advertisement(self, layout: str) -> str:
        if len(layout) == 0:
            raise AdsTemplateException(
                "You must provide the name of a layout under the 'presentations' in your ads JSON file."
            )
        json_data: Dict = self._sphinx_env.sphinx_ads_data
        ads = json_data.get("advertisements")
        presentations: Dict = json_data.get("presentations", default={})
        template_name = presentations.get(layout)["template"]
        jinja_template = self._get_ads_template(template_name)
        html_string: str = ""
        if ads is not None:
            html_string = jinja_template.render(ads=ads.items(), layout=presentations.get(layout))
        return html_string

    def _get_ads_template(self, template_name: str, parent=None, globals=None) -> jinja2.Template:
        """Find and load a template by the name given."""
        return self._env.get_template(template_name, parent=parent, globals=globals)


class AdsTemplateException(SphinxError):
    pass
