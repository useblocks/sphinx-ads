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

extensions = ["sphinx_ads"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output

html_theme = "alabaster"
html_static_path = ["_static"]

pygments_style = "perldoc"

advertisement_path = "./ads.json"
