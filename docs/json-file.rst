.. _json-file:

Ads JSON File
=============

Sphinx-Ads requires an Ad JSON file that contains the advertisement data.
You can provide the JSON file by setting the value for either :ref:`ads_path` or :ref:`ads_url` in your **conf.py** file.

The JSON file must have the following content:

.. code-block:: JSON

    {
        "advertisements": {
          "ad_item_id": {
            "title": "Title for the Ad item",
            "description": "Description for the Ad item",
            "target_url": "URL link to the Ad item"
          }
        },
        "presentations": {
          "layout_name": {
            "template": "Jinja template filename. E.g. horizontal.html",
            "advertisements": "List containing ad item ids for the ads you want to display. E.g. ['ad_item_1', 'ad_item_2']",
            "selector": "A CSS selector to select the HTML element where the ad items will be shown. E.g. .md-nav-primary"
          }
        }

    }


The JSON data is a JSON object which contains the following:

* advertisements (**required**) object
* presentations (**optional**) object

.. code-block:: JSON

    {
        "advertisements": {},
        "presentations": {}
    }

.. note::

    In Python, "object" is analogous to the ``dict`` type and "array" is equivalent to the ``list`` type.

.. _advertisement_obj:

advertisements
--------------

The ``advertisements`` object contains the list of ads you want to include in your project.

In the ``advertisements`` object you can have multiple objects which represent different ad items. Each ad item must have a unique ad ID. Below is an example of ad items in the ``advertisements`` object:

.. code-block:: JSON

    {
        "advertisements": {
            "ad_item_1": {
                "title": "Sphinx Project 1",
                "description": "Sphinx Project 1 is a package that provides dummy text to users."
                "target_url": "https://example.org/sphinx-project-1"
            },
            "sphinx-needs": {
                "title": "Sphinx Needs",
                "description": "Sphinx-Needs is an extension for the Python-based documentation framework Sphinx, which you can simply extend by different extensions to fulfill nearly any requirement of a software development team."
                "target_url": "https://sphinx-needs.readthedocs.io"
            }
        }
    }

Each ad item must consist of the following:

* title (**required**) - a JSON ``str``  that contains the ad's title.
* description (**required**) - a JSON ``str``  that contains the ad's description.
* target_url (**required**) - a JSON ``str``  that contains the ad's URL link.

.. _presentations_obj:

presentations
-------------

The ``presentations`` object contains the list of user-defined layouts you would like to include in your project for displaying the ads.

In the ``presentations`` object you can have multiple objects which represent different layouts. Each layout must have a unique layout name. Below is an example of layouts in the ``presentations`` object:

.. code-block:: JSON

    {
        "presentations": {
            "horizontal": {
                "template": "horizontal.html",
                "advertisements": ["ad_item_1"],
                "selector": "nav.md-nav-primary"
            },
            "vertical": {
                "template": "vertical.html",
                "selector": "div.sphinx_side_bar"
            }
        }
    }

Each ad item must consist of the following:

* template (**required**) - a JSON ``str`` containing the filename of a Jinja template file stored under the **_templates** folder in the Sphinx documentation directory. Refer to the :ref:`Templating <template>` page for more information.
* advertisements (**optional**) - a JSON ``array`` containing ad IDs for the ads you want to display. E.g. ``['ad_item_1', 'ad_item_2']``.
* selector (**required**) - a JSON ``str`` that contains a CSS selector to select where the ad items will be shown on the web page. E.g. ``.md-nav-primary``.

.. note::

    * To select a particular layout, you must pass the layout name to the :ref:`advertisement() <advertisement_func>` function in your **layout.html** file.
    * The JSON file must conform to the JSON schema below.

    .. dropdown:: Sphinx-Ads JSON schema (Draft 7 specification)
        :animate: fade-in-slide-down
        :color: primary

        .. code-block:: JSON

            {
                "$schema": "http://json-schema.org/draft-07/schema#",
                "$id": "http://json-schema.org/draft-07/schema#",
                "title": "ads.json schema",
                "type": "object",
                "properties": {
                    "advertisements": {
                        "type": "object",
                        "patternProperties": {
                            "^.*$": {
                                "type": "object",
                                "properties": {
                                    "title": {
                                        "type": "string",
                                        "minLength": 1
                                    },
                                    "description": {
                                        "type": "string",
                                        "minLength": 1
                                    },
                                    "target_url": {
                                        "type": "string",
                                        "pattern": "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
                                    }
                                },
                                "required": [
                                    "title", "description", "target_url"
                                ]
                            }
                        },
                        "additionalProperties": false
                    },
                    "presentations": {
                        "type": "object",
                        "patternProperties": {
                            "^.*$": {
                                "type": "object",
                                "properties": {
                                    "template": {
                                        "type": "string",
                                        "minLength": 1
                                    },
                                    "advertisements": {
                                        "type": "array",
                                        "items": {
                                            "type": "string",
                                            "minLength": 1
                                        }
                                    },
                                    "selector": {
                                        "type": "string",
                                        "minLength": 1
                                    }
                                },
                                "required": [
                                    "template",
                                    "selector"
                                ]
                            }
                        },
                        "additionalProperties": false
                    }
                },
                "required": [
                    "advertisements"
                ]
            }
