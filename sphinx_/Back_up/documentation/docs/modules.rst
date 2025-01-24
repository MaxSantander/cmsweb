documentation
=============

.. toctree::
   :maxdepth: 4

RIS Backend Modules
===================

Core Components
---------------
1. `pages_app <pages_app/>`_
   - Multi-language CMS implementation
   - Redis cache integration
   - Template-based rendering

Models
------
1. `pages_app.models <pages_app/models/>`_
   - `Page <pages_app/models/page.py>`_: Content management
        - Multi-language support (DE/EN)
        - SEO metadata
        - Publication workflow
   - `Block <pages_app/models/block.py>`_: Content blocks
        - Template-based rendering
        - Image handling
        - Version tracking
   - `MenuItem <pages_app/models/menu_item.py>`_: Navigation
        - Dynamic menu structure
        - Page linking
   - `PageBlock <pages_app/models/page_block.py>`_: Content organization
        - Block positioning
        - Page composition

Views
-----
1. `pages_app.views <pages_app/views/>`_
   - `home.py <pages_app/views/home.py>`_: Main renderer
        - Redis cache implementation
        - Multi-language routing
   - `page.py <pages_app/views/page.py>`_: Page handlers
        - Content assembly
        - Block rendering
   - `page_views.py <pages_app/views/page_views.py>`_: View controllers
        - URL routing
        - Error handling

Configuration
-------------
1. `ris_prj <ris_prj/>`_
   - `settings/ <ris_prj/settings/>`_
        - Development configuration
        - Cache settings
        - Database setup
        - Template configuration

Tests
-----
1. `pages_app.tests <pages_app/tests/>`_
   - Model validation
   - Cache behavior
   - View rendering
   - Multi-language support

Dependencies
------------
- Django 5.0.2
- Redis 5.0.1
- python-dotenv 1.0.1
- WhiteNoise 6.6.0

