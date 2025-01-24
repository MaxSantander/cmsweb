Implementierung
===============

Details der Umsetzung
---------------------
Die Implementierung des Backends umfasst mehrere Kernkomponenten und Technologien, die im Folgenden beschrieben werden.

Page-Modell
-----------
Das Page-Modell ist die zentrale Entität für Webseiteninhalte. Es unterstützt mehrsprachige Inhalte und verwaltet Meta-Informationen.

.. code-block:: python

   from django.db import models

   class Page(models.Model):
       title = models.CharField(max_length=255)
       url_path = models.CharField(max_length=2048)
       language = models.CharField(
           max_length=2,
           choices=[('EN', 'English'), ('DE', 'Deutsch')],
           default='DE',
       )
       meta_description = models.TextField(blank=True, null=True)
       meta_keywords = models.CharField(max_length=255, blank=True, null=True)
       is_published = models.BooleanField(default=False)
       published_at = models.DateTimeField(blank=True, null=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

Block-Modell
------------
Das Block-Modell repräsentiert wiederverwendbare Inhaltskomponenten, die in mehreren Seiten verwendet werden können.

.. code-block:: python

   from django.db import models

   class Block(models.Model):
       template = models.TextField()
       sorting = models.IntegerField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

MenuItem-Modell
---------------
Das MenuItem-Modell verwaltet Navigationsstrukturen und verlinkt Seiten mit anpassbaren Templates.

.. code-block:: python

   from django.db import models

   class MenuItem(models.Model):
       page = models.ForeignKey('Page', on_delete=models.CASCADE)
       template = models.TextField()
       sorting = models.IntegerField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

PageBlock-Modell
----------------
Das PageBlock-Modell verwaltet die Beziehungen zwischen Seiten und Blöcken.

.. code-block:: python

   from django.db import models

   class PageBlock(models.Model):
       page = models.ForeignKey('Page', on_delete=models.CASCADE)
       block = models.ForeignKey('Block', on_delete=models.CASCADE)

Caching
-------
Das Backend implementiert eine effiziente Cache-Strategie, um die Performance zu optimieren. Es wird Redis für das Caching verwendet.

.. code-block:: python

   from django.core.cache import cache
   from django.db.models.signals import post_save, post_delete
   from django.dispatch import receiver

   @receiver([post_save, post_delete], sender=Block)
   @receiver([post_save, post_delete], sender=MenuItem)
   @receiver([post_save, post_delete], sender=PageBlock)
   def invalidate_cache(sender, **kwargs):
       cache.clear()

Django Signals
--------------
Django Signals werden verwendet, um bestimmte Aktionen automatisch auszulösen, wenn Änderungen an den Modellen vorgenommen werden.

.. code-block:: python

   from django.db.models.signals import post_save
   from django.dispatch import receiver
   from .models import Page

   @receiver(post_save, sender=Page)
   def update_page_cache(sender, instance, **kwargs):
       cache_key = f"page_{instance.url_path}_{instance.language}"
       cache.set(cache_key, instance)

Software & Technologien
--------------
    
- **Django-Ökosystem:**
    - Django Framework
    - django-simple-history
    - django-redis
    - django-environ
    - Django Debug Toolbar

- **Datenbank & Caching:**
    - SQLite (Entwicklung)
    - PostgreSQL (Produktion)
    - Redis (Caching-Server)

- **Server & Deployment:**
    - Gunicorn (WSGI)
    - Nginx
    - WhiteNoise
    - systemd

- **Testing & QA:**
    - PyTest & PyTest-Django
    - FactoryBoy
    - Coverage.py

- **Dokumentation:**
    - Sphinx
    - sphinx-rtd-theme
    - sphinxcontrib-plantuml

- **Entwicklungstools:**
    - Python 3.8+
    - PyCharm IDE
    - Git & GitLab
    - make

- **Media & Assets:**
    - Pillow