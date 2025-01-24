Entwurf
=======

Architekturdesign
-----------------
Das Backend verwendet die MTV-Architektur (Model-Template-View), die speziell für Django entwickelt wurde. Diese Architektur trennt die Datenlogik (Model), die Präsentationslogik (Template) und die Steuerlogik (View) klar voneinander.

MTV-Architektur
----------------
Siehe :ref:`mtv-architecture` in den Diagrammen für weitere Details.

ERD-Diagramm
------------
Die Hauptentitäten des ER-Modells sind:

- **Page**: Verwaltung von mehrsprachigen Inhalten.
- **Block**: Wiederverwendbare Inhaltsblöcke.
- **MenuItem**: Navigationselemente.


Systemkomponenten
-----------------
Die wichtigsten Systemkomponenten umfassen:

- **Page**: Zentrale Entität für Webseiteninhalte, speichert mehrsprachige Inhalte (DE/EN) und verwaltet Meta-Informationen.
- **Block**: Enthält Template-basierte Inhaltsblöcke, sortierbare Komponenten und wiederverwendbare Strukturen.
- **MenuItem**: Verwaltet Navigationsstrukturen, template-basierte Menüelemente und sortierbare Menükomponenten.

Beziehungen
-----------
- **Page** (n) hat **Block** (m)
- **Page** (1) hat **MenuItem** (0..1)

Diese Struktur ermöglicht:
- Flexible Seitenerstellung
- Wiederverwendbare Komponenten
- Mehrsprachige Inhalte
- Geordnete Navigation

Datenmodell
-----------
Das Datenmodell umfasst die folgenden Klassen:

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

   class Block(models.Model):
       template = models.TextField()
       sorting = models.IntegerField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

   class MenuItem(models.Model):
       page = models.ForeignKey('Page', on_delete=models.CASCADE)
       template = models.TextField()
       sorting = models.IntegerField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

   class PageBlock(models.Model):
       page = models.ForeignKey('Page', on_delete=models.CASCADE)
       block = models.ForeignKey('Block', on_delete=models.CASCADE)

Cache-Strategie
---------------
Das Backend implementiert eine effiziente Cache-Strategie, um die Performance zu optimieren. Es wird Redis für das Caching verwendet, um schnelle Zugriffszeiten zu gewährleisten.

.. code-block:: python

   from django.core.cache import cache
   from django.db.models.signals import post_save, post_delete
   from django.dispatch import receiver

   @receiver([post_save, post_delete], sender=Block)
   @receiver([post_save, post_delete], sender=MenuItem)
   @receiver([post_save, post_delete], sender=PageBlock)
   def invalidate_cache(sender, **kwargs):
       cache.clear()