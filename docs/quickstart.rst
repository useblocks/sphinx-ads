.. _quickstart:

Quickstart
==========

Eager to get started? This page gives a good introduction to Sphinx-Ads.
Follow :ref:`Installation <install>` to set up a project and install Sphinx-Ads first.

A Minimal Sphinx Docs
---------------------

To setup a Sphinx project, you need to do the following:

1. Install the Sphinx extension using the command:
    .. code-block:: bash

        $ pip install sphinx
2. Setup the Sphinx project by running the following command (choosing the default config options) under a **docs/** folder:
    .. code-block:: bash

        $ sphinx-quickstart

    .. image:: _static/img/image_1.png
        :align: center
        :scale: 70%
        :alt: sphinx-quickstart output
3. Inside the docs folder, you should have the following file structure.
    .. image:: _static/img/image_2.png
        :align: center
        :scale: 90%
        :alt: sphinx file structure
4. Create a JSON file named **ads.json** in your **docs/** folder. The JSON file will contain the advertisement data. For example, you can store the following data in your **ads.json** file.
    .. literalinclude:: ads.json
        :language: JSON
5. In the **conf.py** file under your **docs** folder, you can set the values for the following options:
    .. code-block:: python

        extensions = ["sphinx_ads",]

        ads_path = "ads.json"   # path to the JSON file containing the ad data.
6. Create a **layout.html** in the **_templates/** folder under your **docs/** folder. The HTML file should contain the following:
    .. literalinclude:: _templates/layout.html
        :language: jinja
7. Build the documentation project by running the following command in a terminal inside the **docs** folder:
    .. code-block:: bash

        $ sphinx-build -b html ./ ./_build
8. You can open the HTML build files under the **_build** folder in your browser. The image below shows the **index.html** file in a browser.
    .. image:: _static/img/image_3.png
        :align: center
        :width: 100%
        :alt: index.html file

So what did the above steps do?
