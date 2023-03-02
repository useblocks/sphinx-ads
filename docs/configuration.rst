.. _config:

Configuration
=============

All configurations take place in your project's **conf.py** file.

.. note::

    The defaults for the extension currently supports only the *alabaster* theme.
    You must provide explicit support for your Sphinx theme of choice.

Activation
----------

Add **sphinx_ads** to the extensions list.

.. code-block:: python

   extensions = ["sphinx_ads",]

Create a **layout.html** file in the **_templates/** folder under your **docs/** folder. The HTML file should contain the following data:

.. code-block:: jinja

    {% extends "!layout.html" %}
    {% block footer %}
    {{ super() }}
    {{ advertisement('layout') }}
    {% endblock %}

.. _advertisement_func:

advertisement()
+++++++++++++++

.. autofunction:: sphinx_ads.templates.Template.advertisement

Options
-------

All configuration options starts with the prefix ``ads_`` for **Sphinx-Ads**.

.. _ads_path:

ads_path
++++++++

The ``ads_path`` option allows you to set the path to a locally stored JSON file that contains the advertisement data.

.. note::

   The path must be an absolute or relative path based on the **conf.py** directory. Example: ``ads_path = './ads.json'``

Default: **None**

.. _ads_url:

ads_url
+++++++

The ``ads_url`` option allows you to set the URL of the JSON file that contains the advertisement data.

.. note::

   The URL must return a JSON response containing the advertisement data.
   Example: ``ads_url = 'https://raw.githubusercontent.com/useblocks/sphinx-ads/main/docs/ads.json'``

Default: **None**

The above options are the only options you need to set in your **conf.py** file.

.. note::

   You can set the values for either `ads_path`_ or `ads_url`_ and not both in your **conf.py** file.
