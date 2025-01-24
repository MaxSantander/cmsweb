# Base path for the documentation
base_path = r"C:\Projekte\max_ap\ris_dev\documentation\source\sections"

# Define the content for each .rst file based on the provided files
sections_content = {
    "projektplanung_analyse.rst": """Projektplanung und Analyse
================================

Einleitung
----------
Das Projekt zielt darauf ab, ein Backend für RIS zu entwickeln, das spezifische Anforderungen erfüllt und die Nutzung von allgemeinen Lösungen wie WordPress vermeidet.

Ziele des Projekts
------------------
- Volle Kontrolle über Backend-Funktionen.
- Optimierung der Inhaltsverwaltung.
- Verbesserung der Performance durch Server-seitiges Rendering und Caching.

Projektphasen
-------------
- **Analyse und Planung:** Identifizierung der Anforderungen und Erstellung eines detaillierten Zeitplans.
- **Entwurf:** Auswahl von Django basierend auf einer Nutzwertanalyse.
- **Implementierung:** Entwicklung und Integration von Backend-Funktionen.
- **Tests:** Validierung der Funktionen und Performance.

Technologieauswahl
------------------
Nach einer Analyse wurde Django als Framework gewählt, da es leistungsstarke Features wie ORM, Caching und eine große Community bietet.
    """,
    "entwurf.rst": """Entwurf
=======

Architekturdesign
-----------------
Das Backend verwendet die MTV-Architektur (Model-Template-View).

ERD-Diagramm
------------
Die Hauptentitäten sind:
- **Page:** Verwaltung von mehrsprachigen Inhalten.
- **Block:** Wiederverwendbare Inhaltsblöcke.
- **MenuItem:** Navigationselemente.

.. uml:: _static/uml/erd.puml
    """,
    "implementierung.rst": """Implementierung
===============

Details der Umsetzung
---------------------
- **Page:** Verwaltung von Seiteninhalten.
- **Block:** Wiederverwendbare Inhaltskomponenten.
- **MenuItem:** Navigationselemente.

Signals
-------
Automatische Cache-Invalidierung bei Änderungen an Modellen:

.. code-block:: python

@receiver([post_save, post_delete], sender=Block)
@receiver([post_save, post_delete], sender=MenuItem)
@receiver([post_save, post_delete], sender=PageBlock)
def invalidate_cache(sender, **kwargs):
cache.clear()
    """,
    "test_durchfuehrung.rst": """Test und Durchführung
====================

Tests
-----
- **Unit Tests:** Überprüfung einzelner Funktionen.
- **Integrationstests:** Validierung der Interaktion zwischen Modulen.
- **Manuelle Tests:** Überprüfung der Benutzeroberfläche.

Qualitätsanforderungen
----------------------
- **Funktionalität:** Mehrsprachigkeit, Cache-Management.
- **Performance:** Ladezeit < 2 Sekunden.
- **Wartbarkeit:** Dokumentierter Code und modulare Architektur.
    """,
    "glosar.rst": """Glosar
======

.. glossary::

Backend
Der Teil einer Anwendung, der für Datenverarbeitung und Logik zuständig ist.

Frontend
Der Teil einer Anwendung, der für die Benutzerschnittstelle verantwortlich ist.

ORM
Object-Relational Mapping, eine Technik, um Datenbankabfragen in Code zu integrieren.
    """,
    "diagramme.rst": """Diagramme
=========

Diagramme des Projekts:
- **Use Case Diagramm**:
.. uml:: _static/uml/use_case.puml

- **ERD Diagramm**:
.. uml:: _static/uml/erd.puml

- **MTV Architektur**:
.. uml:: _static/uml/mtv_architecture.puml
    """,
    "bilder.rst": """Bilder
======

Hier können zusätzliche Bilder zur Veranschaulichung eingefügt werden.
    """,
}

# Ensure the base path exists
os.makedirs(base_path, exist_ok=True)

# Write the content to each .rst file
for file_name, content in sections_content.items():
    file_path = os.path.join(base_path, file_name)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

# Confirmation message
print(f".rst files have been successfully created in {base_path}")



#  # strucrture creator
# import os
#
# def create_project_structure():
#     base_dir = r"C:\\Projekte\\max_ap\\ris_dev\\documentation"
#
#     # Define folder structure
#     folders = [
#         f"{base_dir}/source",
#         f"{base_dir}/source/sections",
#         f"{base_dir}/source/_static",
#         f"{base_dir}/source/_templates",
#     ]
#
#     # Define files and their initial content
#     files = {
#         f"{base_dir}/source/conf.py": """# Configuration for Sphinx documentation
# project = 'RIS Backend Dokumentation'
# author = 'Max Santander'
# version = '1.0'
# release = '1.0'
# extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo', 'sphinx.ext.viewcode']
# templates_path = ['_templates']
# exclude_patterns = []
# language = 'de'
# html_theme = 'alabaster'
#         """,
#         f"{base_dir}/source/index.rst": """RIS Backend Dokumentation
# =================================
#
# .. toctree::
# :maxdepth: 2
# :caption: Inhalt
#
# sections/projektplanung_analyse
# sections/entwurf
# sections/implementierung
# sections/test_durchfuehrung
#
# sections/glosar
# sections/diagramme
# sections/bilder
#         """,
#         f"{base_dir}/source/sections/projektplanung_analyse.rst": """Projektplanung und Analyse
# ================================
#
# Diese Sektion beschreibt die Planung und Analysephase des Projekts, einschließlich Zielsetzung und Zeitplanung.
#         """,
#         f"{base_dir}/source/sections/entwurf.rst": """Entwurf
# =======
#
# In dieser Sektion wird der Entwurf des Backends beschrieben, einschließlich der Systemarchitektur und der Datenbankstruktur.
#         """,
#         f"{base_dir}/source/sections/implementierung.rst": """Implementierung
# ===============
#
# Hier werden die technischen Details der Umsetzung und wichtige Entwicklungsentscheidungen dokumentiert.
#         """,
#         f"{base_dir}/source/sections/test_durchfuehrung.rst": """Test und Durchführung
# ====================
#
# Diese Sektion umfasst die Testmethoden, Ergebnisse und Validierungsschritte.
#         """,
#         f"{base_dir}/source/sections/glosar.rst": """Glosar
# ======
#
# Ein Glossar mit Definitionen von technischen Begriffen und Konzepten.
#         """,
#         f"{base_dir}/source/sections/diagramme.rst": """Diagramme
# =========
#
# Diese Sektion enthält die Diagramme des Projekts, einschließlich UML-Diagramme und Architekturmodelle.
#
# .. uml:: _static/uml/use_case.puml
#
# .. uml:: _static/uml/erd.puml
#
# .. uml:: _static/uml/mtv_architecture.puml
#         """,
#         f"{base_dir}/source/sections/bilder.rst": """Bilder
# ======
#
# Diese Sektion enthält zusätzliche Bilder, die das Projekt illustrieren.
#         """,
#         f"{base_dir}/Makefile": """# Makefile für die Dokumentation
# html:
# \tmake -C source html
#
# latexpdf:
# \tmake -C source latexpdf
#         """,
#         f"{base_dir}/make.bat": """@echo off
# if "%1" == "html" make -C source html
# if "%1" == "latexpdf" make -C source latexpdf
#         """,
#     }
#
#     # Create directories
#     for folder in folders:
#         os.makedirs(folder, exist_ok=True)
#
#     # Create files with initial content
#     for file_path, content in files.items():
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)
#         with open(file_path, 'w', encoding='utf-8') as file:
#             file.write(content)
#
#     print("Documentation structure created successfully.")
#
# create_project_structure()
