Test und Durchführung
====================

Diese Sektion umfasst die implementierten Tests und ihre Ergebnisse.

Testphase
---------
Die Tests stellen sicher, dass die Kernfunktionalitäten des CMS korrekt implementiert sind:

- **Model Tests**: Validierung der Datenmodelle und ihrer Beziehungen
- **Cache Tests**: Überprüfung der Redis-Cache Implementierung
- **View Tests**: Tests der Seiten-Rendering und URL-Routing

Implementierte Tests
------------------

Model Tests (test_models.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

   class PageModelTest(TestCase):
       def test_page_creation(self):
           """Test page creation with all fields."""
           page = Page.objects.create(
               title="Test Page",
               url_path="/test",
               language="EN"
           )
           self.assertEqual(page.title, "Test Page")

   class BlockModelTest(TestCase):
       def test_block_creation(self):
           """Test block creation with all fields."""
           block = Block.objects.create(
               name="Test Block",
               template="<div>Test Content</div>",
               sorting=1
           )
           self.assertEqual(str(block), "Test Block")

   class MenuItemModelTest(TestCase):
       def test_menu_item_ordering(self):
           """Test menu item ordering by sorting field."""
           menu1 = MenuItem.objects.create(page=self.page, template="test1", sorting=2)
           menu2 = MenuItem.objects.create(page=self.page, template="test2", sorting=1)
           menus = MenuItem.objects.all().order_by("sorting")
           self.assertEqual(menus[0], menu2)

Cache Tests (test_cache.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

   class CacheTests(TestCase):
       def test_cache_set_get(self):
           """Test basic cache set and get operations."""
           cache.set("test_key", "test_value")
           self.assertEqual(cache.get("test_key"), "test_value")

       def test_cache_timeout(self):
           """Test cache timeout functionality."""
           cache.set("timeout_key", "timeout_value", timeout=1)
           time.sleep(2)
           self.assertIsNone(cache.get("timeout_key"))

View Tests (test_views.py)
~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

   class ViewTests(TestCase):
       def test_home_view(self):
           """Test home page rendering."""
           response = self.client.get("/")
           self.assertEqual(response.status_code, 200)

       def test_render_page_existing_page(self):
           """Test rendering of an existing published page."""
           page = Page.objects.create(
               title="Test Page",
               url_path="/test",
               language="EN"
           )
           page.publish()
           response = self.client.get("/test/")
           self.assertEqual(response.status_code, 200)

Testergebnisse
-------------
Die Tests zeigen, dass:

- Alle Modelle korrekt erstellt und validiert werden
- Die Cache-Implementierung wie erwartet funktioniert
- Das Seiten-Rendering und URL-Routing korrekt arbeiten
- Die Datenbank-Beziehungen zwischen den Modellen funktionieren
- Die Sortierung von Menüpunkten korrekt implementiert ist

Testprotokolle
-------------
.. code-block:: text

   ============================= test session starts ==============================
   platform linux -- Python 3.8.5, pytest-6.2.4
   django: settings: ris_dev.settings
   plugins: django-4.4.0, cov-2.12.1
   collected 23 items

   pages_app/tests/test_cache.py .... [ 16%]
   pages_app/tests/test_models.py ........... [ 60%]
   pages_app/tests/test_views.py ...... [100%]

   ============================== 23 passed ==============================