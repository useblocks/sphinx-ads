.. _changelog:

Changelog & License
===================

License
-------

.. include:: ../LICENSE

0.0.1
-----

Released: under development

* **27.02.2023** - Added both Python and JavaScript testcases for the extension and added the JavaScript test CI action.
* **24.02.2023** - Bugfix: Fixed bug in Sphinx-Ads JavaScript code to run only when the HTML document has loaded
* **21.02.2023** - Added the following changes for the preparation of an official first release:
    * Added the GitHub Action workflows to handle documentation build, extension release, and pull requests checks
    * Updated the documentation
    * Minor changes to extension code
* **13.02.2023** - Added the following changes:
    * Wrote the documentation for Sphinx-Ads
    * Wrote the JS and CSS code for the default carousel layout
* **11.02.2023** - Added JavaScript to move pre-generated HTML code to the needed HTML destination and made some minor changes.
* **05.02.2023** - Added function to check ads configuration variables
* **03.02.2023** - Added the Template class which contains the following methods:
    * Method to provide the paths to the Jinja templates
    * Method to retrieve Jinja templates
    * Method to return advertisement HTML based on layout
* **26.01.2023** - Added the :ref:`ads_path` and :ref:`ads_url` configuration options and the functions to load JSON data from path or url
* **25.01.2023** - Setup Sphinx-Ads project and configure documentation