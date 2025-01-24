Home View Documentation 
=====================

Overview
--------
The home view module implements the main page rendering logic for the RIS CMS, including caching and language support.

.. module:: pages_app.views.home
   :synopsis: Main view handling for RIS CMS

Key Functions
------------

render_page
~~~~~~~~~~
.. autofunction:: pages_app.views.home.render_page

Cache Implementation 
------------------
The view implements Redis caching with the following features:

* Language-specific caching
* Page content caching
* Cache invalidation on content updates

.. code-block:: python

   # Cache key format
   cache_key = f"page_{normalized_path}_{language}"

Dependencies
-----------
* :mod:`django.shortcuts`
* :mod:`django.utils.translation`
* :mod:`django.core.cache`
* :mod:`pages_app.models`

Models Used
----------
* :class:`pages_app.models.Page`
* :class:`pages_app.models.Block`
* :class:`pages_app.models.MenuItem`
* :class:`pages_app.models.PageBlock`

Configuration
------------
Cache settings are defined in :file:`ris_prj/settings/base.py`:

.. code-block:: python

   CACHES = {
       'default': {
           'BACKEND': 'django_redis.cache.RedisCache',
           'LOCATION': 'redis://127.0.0.1:6379/1',
           'OPTIONS': {
               'CLIENT_CLASS': 'django_redis.client.DefaultClient',
           }
       }
   }