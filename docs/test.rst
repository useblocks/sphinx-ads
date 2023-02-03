SA - Sphinx Advertisement
=========================

Problem / Challenge
-------------------
I need a way to show links to other projects in our documentation of our Open-Source Projects.
So Sphinx-Needs should contain advertisements for Sphinx-SimplePdf and the other way around.

The config and targets shall not be configured hardly in the related doc project.
Instead, an open and free available json-file, which is maintained in one repo, shall be downloaded via javascript and create the advertisements on the fly.

This could be also a new generic Sphinx extension: Sphinx-Advertising.

Concept
-------
Advertisement data is retrieved/generated during a sphinx-Build.

Config stored ``advertisement.json``, this can be stored local or (in most cases) in a server.
User needs to provide a path or an url.

For ``conf.py`` we have a new option: ``advertisement_path`` or ``advertisement_url``

jinja-function ``advertisement(layout)``, needs also to be made public in the Jinja environment.

Workflow:

1. Sphinx and extension starts build
2. SA loads ``advertisement.json``
3. SA gets images
    a. Maybe copy it from local or download it from url
    b. Store it in ``_static/_advertisements/images``
4. (Copy ``advertisement.json`` to ``_static/_advertisements``)
5. Copy ``advertisement.js`` to ``_static/_advertisements``.  And register in Sphinx
6. Copy ``advertisement.css`` to ``_static/_advertisements``. And register in Sphinx
7. Get executed by the builder by ``advertisement(layout)`` in jinja
    a. Prepare data
    b. Render own jinja template from advertisement.json
    c. Return generated HTML

Conf format
-----------

.. code-block:: JSON

    {
    "advertisements":
      "product_1": {
        "image": {
          "path": "../image.png",
          "url": "server.com/image.png"
        "title": "sdfsdfsd",
        "description": "....",
        "target_url": "new-product.com/awesome"
        }
      },
      "product_2": "{...}",
      "product_3": "{...}",
    },
    "presentations": {
      "my_list": {
        "template": "list_template.html",
        "images": {
          "width": 200,
          "height": 300,
        },
        "advertisements": ["product_1", "product_3"],
        "selector": "div.ADS_LOCATION"
      },
      "card_xyz": {"# with different advertisements"}
    }

    }

Template format
---------------

Inside _templates/main.html

.. code-block:: HTML

    {% include base.html %}
    ....

    {% advertisment(layout) %}
    # layout may be list, card, ...



Tasks
-----

- Create a new repo (Daniel)
- Set up a doc project
- Write a first technical concept (one-pager) and discuss it

Definition of Done
------------------
- Concept is ready