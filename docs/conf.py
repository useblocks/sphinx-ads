# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.append(os.path.abspath("../sphinx_ads"))

project = "Sphinx-Ads"
copyright = "2023, team useblocks"
author = "team useblocks"
release = "0.0.1"

extensions = [
    "sphinx_ads",
    "sphinx.ext.autodoc",
    "sphinx_design",
    # "sphinx_immaterial",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output

html_favicon = "_static/img/favicon.ico"
html_logo = "_static/img/sphinx-ads-logo.png"
html_theme = "alabaster"
# html_theme = "sphinx_immaterial"
html_title = "Sphinx-Ads Docs"
html_static_path = ["_static"]

pygments_style = "perldoc"

ads_path = "./ads.json"
# ads_url = "https://raw.githubusercontent.com/useblocks/sphinx-ads/main/docs/ads.json"
