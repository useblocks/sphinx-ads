.. _template:

Templating
==========

Sphinx-Ads allows you to write your own `Jinja <http://jinja.pocoo.org/>`_ template files which you can use in your layouts to customise how you want to display your ads.

You assign the template filename as a value to the ``template`` key under a layout. For example, if you create a template called **my-custom-template.html**, you can use it like this under the :ref:`presentation <presentations_obj>` object in your ad JSON file:

.. code-block:: JSON

    {
        "presentations": {
            "horizontal": {
                "template": "my-custom-template.html",
            }
        }
    }

.. note::

    * You should store the template file under the **_templates** folder in your Sphinx documentation directory.
    * You should have one of the following file extensions: *.html*, *.jinja2*, or *.j2*.

The plugin provides the following variables which you can use in your custom Jinja template:

* ads - a Python set-like object containing the key/value pairs (i.e. (ad_ID, ad_value)) of the :ref:`advertisement <advertisement_obj>` data. Example of the ``ads`` object:
    .. code-block:: python

        ads = dict_items([('sphinx_needs', {'title': 'Sphinx Needs', 'description': 'Sphinx-Needs is an extension for the Python-based documentation framework Sphinx, which you can simply extend by different extensions to fulfill nearly any requirement of a software development team.', 'target_url': 'https://sphinx-needs.readthedocs.io'})])
* layout - a dictionary object containing the following information about the layout you selected:
    * template - a ``str`` containing the filename of a Jinja template file.
    * advertisements - ``list`` containing ad IDs for the ads you want to display.
    * selector - a ``str`` that contains a CSS selector to select where the ad items will be shown on the web page.

.. dropdown:: Example of a custom Jinja template file
    :animate: fade-in-slide-down
    :color: primary

    .. code-block:: jinja

        {% if ads %}
        {% set ads_to_show = layout.advertisements %}
        {% if ads_to_show %}
            {% for ad_key, ad_value in ads %}
                {% if ad_key in ads_to_show and ad_value is mapping %}
                    <div id="ads_link_{{ loop.index }}" class="sphinx-ads-item sa_is_hidden">
                        <a href="{{ ad_value.get('target_url') }}" title="{{ ad_value.get('title') }}">
                            <b style="margin-bottom: 3px;">{{ ad_value.get('title') }}</b>
                            <p>{{ ad_value.get('description') | truncate(60) }}</p>
                        </a>
                    </div>
                {% endif %}
            {% endfor %}
        {% else %}
            {% for ad_key, ad_value in ads %}
                {% if ad_value is mapping %}
                    <div id="ads_link_{{ loop.index }}" class="sphinx-ads-item sa_is_hidden">
                        <a href="{{ ad_value.get('target_url') }}" title="{{ ad_value.get('title') }}">
                            <b style="margin-bottom: 3px;">{{ ad_value.get('title') }}</b>
                            <p>{{ ad_value.get('description') | truncate(60) }}</p>
                        </a>
                    </div>
                {% endif %}
            {% endfor %}
        {% endif %}
        {% endif %}
