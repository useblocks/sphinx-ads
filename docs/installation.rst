.. _install:

Installation
============

Python Version
--------------
We recommend using the latest version of Python. Sphinx-Ads supports Python 3.7 and newer.

Virtual environments
--------------------
Use a virtual environment to manage the dependencies for your project, both in development and in production.

Python comes bundled with the `venv <https://docs.python.org/3/library/venv.html#module-venv>`_
module to create virtual environments.

Create an environment
+++++++++++++++++++++
Create a project folder and a ``venv`` folder within:

.. tab-set::

    .. tab-item:: macOS/Linux
        :sync: unix

        .. code-block:: bash

            $ mkdir myproject
            $ cd myproject
            $ python3 -m venv .venv

    .. tab-item:: Windows
        :sync: win

        .. code-block:: posh

            > mkdir myproject
            > cd myproject
            > python -m venv .venv

Activate the environment
++++++++++++++++++++++++
Before you work on your project, activate the corresponding environment:

.. tab-set::

    .. tab-item:: macOS/Linux
        :sync: unix

        .. code-block:: bash

            $ .venv/bin/activate

    .. tab-item:: Windows
        :sync: win

        .. code-block:: posh

            > .venv\Scripts\activate

Install Sphinx-Ads
------------------
Within the activated environment, use the following command to install Sphinx-Ads:

.. tab-set::

    .. tab-item:: Using pip

        .. code-block:: bash

           $ pip install sphinx-ads

    .. tab-item:: From source

        .. code-block:: bash

           $ git clone https://github.com/useblocks/sphinx-ads
           $ cd sphinx-ads
           $ pip install .


You can refer to the :ref:`Quickstart <quickstart>` section for a good introduction to Sphinx-Ads.