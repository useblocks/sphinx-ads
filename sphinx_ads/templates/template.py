# import os
from pathlib import Path
from typing import Any, Dict, List, Union

import jinja2
from sphinx.application import Sphinx
from sphinx.errors import SphinxError

from sphinx_ads.logging import get_logger
from sphinx_ads.templates.layout import sphinx_ads_layouts

logger = get_logger(__name__)


class Template:
    def __init__(self, app: Sphinx):
        self._sphinx_app = app
        self._template_files: List[Path] = []
        self._jinja_env = app.builder.templates.environment

    @property
    def template_files(self) -> List[Path]:
        base_path = Path(Path(__file__).parent).resolve()  # Path to folder containing default template files
        template_paths = []

        docs_src_dir = Path(self._sphinx_app.confdir)  # Path to folder containing custom template files

        if docs_src_dir.is_dir():
            template_paths.append(docs_src_dir)
        template_paths.append(base_path.joinpath("."))

        return template_paths

    def advertisement(self, layout: str = "sphinx-ads-default") -> str:
        """
        Function to generate the advertisement HTML content you want to display in your web browser.

        :param layout: Name of the layout you want to use when presenting the advertisement content.
                        Default layout is ``sphinx-ads-default``. The value must correspond to one of the layouts in
                        your ads JSON file or the default layout is used.
        :return: The advertisement HTML content
        """
        if len(layout) == 0:
            raise AdsTemplateException(
                "You must provide the name of a layout under the 'presentations' in your ads JSON file."
            )
        json_data: Dict[str, Dict[str, Any]] = self._sphinx_app.env.sphinx_ads_data
        ads = json_data.get("advertisements")
        presentations: Dict[str, Union[str, Dict]] = json_data.get("presentations")
        layout_data: Dict = presentations.get(layout) or sphinx_ads_layouts.get(layout, {})
        template_name: str = layout_data.get("template", "sphinx_ads_default.html")
        jinja_template = self.get_ads_template(template_name)
        jinja_html_string = ""
        if ads is not None:
            jinja_html_string = jinja_template.render(ads=ads.items(), layout=layout_data)

        html_string: str = (
            f"<div id='sphinx_ads' style='display:none;margin-top:5px;padding:0 2px' "
            f"data-sphinx-ads-docs-html_theme='{self._sphinx_app.config.html_theme}' "
            f"data-sphinx-ads-selector='{layout_data.get('selector', 'div.sphinxsidebar')}'>"
            f"{jinja_html_string}"
            '<div style="text-align:right;margin-bottom:10px;font-size:10pt;color:#787878;">'
            "<i> With 💛 by&nbsp;<a "
            'href="https://sphinx-ads.useblocks.com/">Sphinx-Ads</a></i></div>'
            f"</div>"
        )

        return html_string

    def get_ads_template(self, template_name: str) -> jinja2.Template:
        """Load a template by the name given."""
        jinja_template: jinja2.Template = self._jinja_env.get_template(template_name)
        return jinja_template


class AdsTemplateException(SphinxError):
    pass
