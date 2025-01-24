Page Views Documentation
======================

Overview
--------
Documentation for the page-specific views in the RIS CMS.

.. module:: pages_app.views.page
   :synopsis: Page-specific view handling

Key Components
-------------

Page Rendering
~~~~~~~~~~~~~
.. autofunction:: pages_app.views.home.render_page

Main view function that handles page rendering with:
- Multi-language support (DE/EN)
- Redis caching implementation
- Dynamic block loading

Page Model Integration
~~~~~~~~~~~~~~~~~~~~
Integrates with:

- :class:`pages_app.models.Page` - Core content model
- :class:`pages_app.models.Block` - Reusable content blocks
- :class:`pages_app.models.MenuItem` - Navigation elements

Cache Configuration
-----------------
Uses Redis for caching with:

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

Dependencies
-----------
- Django Views Framework
- Redis Cache Backend
- Language Middleware