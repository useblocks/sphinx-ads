.. _config:

Configuration
=============

All configurations take place in your project's **conf.py** file.

Activation
----------

Add **sphinx_ads** to the extensions list.

.. code-block:: python

   extensions = ["sphinx_ads",]

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
   Example: ``ads_url = 'https://raw.githubusercontent.com/useblocks/sphinx-advertising/main/docs/ads.json'``

Default: **None**

The above options are the only options you need to set in your **conf.py** file.

.. note::

   You cannot set the values for both `ads_path`_ and `ads_url`_ in the **conf.py** file.
   The extension only needs one of the options set in your **conf.py** file.