from typing import Any, Dict, List, Optional

import jinja2
from sphinx.application import Sphinx
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.config import Config
from sphinx.environment import BuildEnvironment
from sphinx.errors import SphinxError

from sphinx_ads.logging import get_logger

# from sphinx_ads.directives.advertisement import AdsDirective
from sphinx_ads.templates import Template
from sphinx_ads.utils import get_json_data_from_path, get_json_data_from_url, load_data

VERSION = "0.0.1"


def setup(app: Sphinx) -> Dict[str, Any]:
    log = get_logger(__name__)
    log.debug("Starting setup of Sphinx-Ads")

    ########################################################################
    # CONFIG_VALUES
    ######################################################################
    # Define config values
    app.add_config_value("advertisement_path", None, "html", types=[str])
    app.add_config_value("advertisement_url", None, "html", types=[str])

    ########################################################################
    # DIRECTIVES
    ########################################################################

    # Define directives
    # app.add_directive("sphinx-ads", AdsDirective)

    ########################################################################
    # EVENTS
    ########################################################################
    # Make connections to events
    app.connect("config-inited", check_configuration)
    app.connect("builder-inited", builder_inited)
    # app.connect("env-before-read-docs", prepare_env)

    return {
        "version": VERSION,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def builder_inited(app: Sphinx) -> None:
    """Create Jinja env and global advertisement() function"""
    if not hasattr(app.env, "sphinx_ads_data"):
        # Used to store the Ads json data, so it can be easily accessible anywhere in the extension.
        app.env.sphinx_ads_data = {}

    load_data(app)  # Loads the json data and updates env.sphinx_ads_data

    if isinstance(app.builder, StandaloneHTMLBuilder):
        template = Template(app)
        app.builder.templates.loaders.append(jinja2.FileSystemLoader(template.template_files))
        app.builder.templates.environment.globals["advertisement"] = template.advertisement


# def prepare_env(app: Sphinx, env: BuildEnvironment, _docname: str) -> None:
#     """
#     Prepares the sphinx environment to store sphinx-ads JSON data.
#     """
#     if not hasattr(env, "sphinx_ads_data"):
#         # Used to store the Ads json data, so it can be easily accessible anywhere in the extension package.
#         env.sphinx_ads_data = {}
#
#     if app.config.advertisement_path is not None and len(app.config.advertisement_path) != 0:
#         ads_json_data: Dict = get_json_data_from_path(app)
#         env.sphinx_ads_data.update(ads_json_data)
#
#     if app.config.advertisement_url is not None and len(app.config.advertisement_url) != 0:
#         ads_json_data: Dict = get_json_data_from_url(app)
#         env.sphinx_ads_data.update(ads_json_data)
#

def check_configuration(app: Sphinx, config: Config) -> None:
    """
    Checks the configuration options.
    """
    if (not config["advertisement_path"] and not config["advertisement_url"]) or (
        config["advertisement_path"] and config["advertisement_url"]
    ):
        raise AdsConfigException(
            "Please provide a path or url to retrieve the JSON data from "
            "using either the 'advertisement_path' or 'advertisement_url' variable."
        )

    if config["advertisement_path"] and config["advertisement_url"]:
        raise AdsConfigException(
            "Please provide only one of these variables: 'advertisement_path' or 'advertisement_url' variable."
        )


class AdsConfigException(SphinxError):
    pass
