from typing import Any, Dict, List

from sphinx.application import Sphinx
from sphinx.errors import SphinxError

from sphinx_ads.directives.advertisement import AdsDirective
from sphinx_ads.logging import get_logger

VERSION = "0.0.1"


def setup(app: Sphinx) -> Dict[str, Any]:
    log = get_logger(__name__)
    log.debug("Starting setup of Sphinx-Needs")
    log.debug("Load Sphinx-Data-Viewer for Sphinx-Needs")

    app.add_config_value("needs_include_needs", True, "html", types=[bool])
    app.add_config_value("needs_need_name", "Need", "html", types=[str])

    ########################################################################
    # DIRECTIVES
    ########################################################################

    # Define directives
    app.add_directive("sphinx-ads", AdsDirective)

    return {
        "version": VERSION,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


class AdsConfigException(SphinxError):
    pass
