Sphinx-Ads
==========

.. image:: https://img.shields.io/pypi/dm/sphinx-ads.svg
    :target: https://pypi.python.org/pypi/sphinx-ads
    :alt: Downloads
.. image:: https://img.shields.io/pypi/l/sphinx-ads.svg
   :target: https://pypi.python.org/pypi/sphinx-ads
   :alt: License
.. image:: https://img.shields.io/pypi/pyversions/sphinx-ads.svg
   :target: https://pypi.python.org/pypi/sphinx-ads
   :alt: Supported versions
.. image:: https://github.com/useblocks/sphinx-ads/actions/workflows/docs.yaml/badge.svg
   :target: https://github.com/useblocks/sphinx-ads/actions/docs.yaml
   :alt: GitHub Docs CI Action status
.. image:: https://github.com/useblocks/sphinx-ads/actions/workflows/ci.yaml/badge.svg
   :target: https://github.com/useblocks/sphinx-ads/actions
   :alt: GitHub CI Action status
.. image:: https://img.shields.io/pypi/v/sphinx-ads.svg
   :target: https://pypi.python.org/pypi/sphinx-ads
   :alt: PyPI Package latest release
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: black code style


Sphinx-Ads is an extension for the `Python <https://python.org>`_ based documentation framework `Sphinx <https://www.sphinx-doc.org>`_, which you can use to add advertisements from a central source to your Sphinx documentation website.

* Docs: http://sphinx-ads.useblocks.com
* Repo: https://github.com/useblocks/sphinx-ads

Installation
------------

We recommend using the latest version of Python. Sphinx-Ads supports Python 3.7 and newer.
Also, we recommend using a virtual environment to manage the dependencies for your project, both in development and production.

Using pip
+++++++++

.. code-block:: bash

    $ pip install sphinx-ads

From source
+++++++++++

.. code-block:: bash

    $ git clone https://github.com/useblocks/sphinx-ads
    $ cd sphinx-ads
    $ pip install .

Activation
++++++++++

In the **conf.py** file under your **docs** folder, you can set the values for the following options:

.. code-block:: python

    extensions = ["sphinx_ads",]

    ads_path = "ads.json"   # path to the JSON file containing the ad data.
    ads_url = "https://example.org/ads.json"    # url link to the JSON data

.. note::

    * You can set the values for either ``ads_path`` or ``ads_url`` and not both in your **conf.py** file.
    * Refer to the `Ads JSON file <http://sphinx-ads.useblocks.com/json-file.html>`_ documentation page for more information about the JSON file's data.

Create a **layout.html** file in the **_templates/** folder under your **docs/** folder. The HTML file should contain the following data:

.. code-block:: jinja

    {% extends "!layout.html" %}
    {% block footer %}
    {{ super() }}
    {{ advertisement() }}
    {% endblock %}
