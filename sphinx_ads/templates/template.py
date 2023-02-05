# import os
from pathlib import Path
from typing import Dict, Optional

import jinja2
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.errors import SphinxError

from sphinx_ads.logging import get_logger

logger = get_logger(__name__)


class Template:
    def __init__(self, app: Sphinx):
        self._sphinx_app = app
        self._template_files = []
        self._jinja_env = app.builder.templates.environment

    @property
    def template_files(self):
        base_path = Path(Path(__file__).parent).resolve()  # Path to folder containing default template files
        template_paths = []

        docs_src_dir = Path(self._sphinx_app.confdir)  # Path to folder containing custom template files

        if docs_src_dir.is_dir():
            template_paths.append(docs_src_dir)
        template_paths.append(base_path.joinpath("."))

        return template_paths

    def advertisement(self, layout: str) -> str:
        if len(layout) == 0:
            raise AdsTemplateException(
                "You must provide the name of a layout under the 'presentations' in your ads JSON file."
            )
        json_data: Dict = self._sphinx_app.env.sphinx_ads_data
        ads = json_data.get("advertisements")
        presentations: Dict = json_data.get("presentations")
        template_name: str = presentations.get(layout)["template"] if presentations is not None else {}
        jinja_template = self.get_ads_template(template_name)
        html_string: str = ""
        if ads is not None:
            html_string = jinja_template.render(ads=ads.items(), layout=presentations.get(layout))
        return html_string

    def get_ads_template(self, template_name: str) -> jinja2.Template:
        """Load a template by the name given."""
        return self._jinja_env.get_template(template_name)


class AdsTemplateException(SphinxError):
    pass
