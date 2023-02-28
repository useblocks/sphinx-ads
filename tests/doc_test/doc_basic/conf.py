# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os

# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "basic test"
copyright = "2022, team useblocks"
author = "team useblocks"

extensions = ["sphinx_ads"]

templates_path = ["_templates"]

html_theme = "alabaster"

ads_url = "https://raw.githubusercontent.com/useblocks/sphinx-ads/main/docs/ads.json"
