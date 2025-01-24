Examples
========

API Usage Examples
----------------

Page Creation
~~~~~~~~~~~~
.. code-block:: python

   # Create a new page
   from pages_app.models import Page

   page = Page.objects.create(
       title="Example Page",
       url_path="/example",
       language="EN",
       is_published=True
   )

Block Management
~~~~~~~~~~~~~~
.. code-block:: python

   # Add a block to a page
   from pages_app.models import Block, PageBlock

   block = Block.objects.create(
       name="Header Block",
       sorting=1
   )

   PageBlock.objects.create(
       page=page,
       block=block
   )

Cache Operations
~~~~~~~~~~~~~~
.. code-block:: python

   # Cache management example
   from django.core.cache import cache

   # Cache a page
   cache_key = f"page_{page.url_path}_{page.language}"
   cache.set(cache_key, page_data, timeout=3600)
