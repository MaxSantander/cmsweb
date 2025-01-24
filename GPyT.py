import os

def create_project_structure():
    base_dir = r"C:\\Projekte\\max_ap\\ris_dev\\documentation"

    # Define folder structure
    folders = [
        f"{base_dir}/source",
        f"{base_dir}/source/sections",
        f"{base_dir}/source/_static",
        f"{base_dir}/source/_templates",
    ]

    # Define files and their initial content
    files = {
        f"{base_dir}/source/conf.py": """# Configuration for Sphinx documentation
project = 'RIS Backend Dokumentation'
author = 'Max Santander'
version = '1.0'
release = '1.0'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo', 'sphinx.ext.viewcode']
templates_path = ['_templates']
exclude_patterns = []
language = 'de'
html_theme = 'alabaster'
        """,
        f"{base_dir}/source/index.rst": """RIS Backend Dokumentation
=================================

.. toctree::
:maxdepth: 2
:caption: Inhalt

sections/projektplanung_analyse
sections/entwurf
sections/implementierung
sections/test_durchfuehrung

sections/glosar
sections/diagramme
sections/bilder
        """,
        f"{base_dir}/source/sections/projektplanung_analyse.rst": """Projektplanung und Analyse
================================

Diese Sektion beschreibt die Planung und Analysephase des Projekts, einschließlich Zielsetzung und Zeitplanung.
        """,
        f"{base_dir}/source/sections/entwurf.rst": """Entwurf
=======

In dieser Sektion wird der Entwurf des Backends beschrieben, einschließlich der Systemarchitektur und der Datenbankstruktur.
        """,
        f"{base_dir}/source/sections/implementierung.rst": """Implementierung
===============

Hier werden die technischen Details der Umsetzung und wichtige Entwicklungsentscheidungen dokumentiert.
        """,
        f"{base_dir}/source/sections/test_durchfuehrung.rst": """Test und Durchführung
====================

Diese Sektion umfasst die Testmethoden, Ergebnisse und Validierungsschritte.
        """,
        f"{base_dir}/source/sections/glosar.rst": """Glosar
======

Ein Glossar mit Definitionen von technischen Begriffen und Konzepten.
        """,
        f"{base_dir}/source/sections/diagramme.rst": """Diagramme
=========

Diese Sektion enthält die Diagramme des Projekts, einschließlich UML-Diagramme und Architekturmodelle.

.. uml:: _static/uml/use_case.puml

.. uml:: _static/uml/erd.puml

.. uml:: _static/uml/mtv_architecture.puml
        """,
        f"{base_dir}/source/sections/bilder.rst": """Bilder
======

Diese Sektion enthält zusätzliche Bilder, die das Projekt illustrieren.
        """,
        f"{base_dir}/Makefile": """# Makefile für die Dokumentation
html:
\tmake -C source html

latexpdf:
\tmake -C source latexpdf
        """,
        f"{base_dir}/make.bat": """@echo off
if "%1" == "html" make -C source html
if "%1" == "latexpdf" make -C source latexpdf
        """,
    }

    # Create directories
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Create files with initial content
    for file_path, content in files.items():
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    print("Documentation structure created successfully.")

create_project_structure()
