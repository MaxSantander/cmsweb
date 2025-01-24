# Configuration file for the Sphinx documentation builder.

import os
import sys
import django

# Add the project's source directory to the Python path
sys.path.insert(0, os.path.abspath('../..'))  # Fix path relative to conf.py

# Configure Django Settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ris_prj.settings.development')
django.setup()

# Project information
project = 'RIS Backend Documentation'
author = 'Maximiliano Santander'
release = '1.0'
version = '1.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',         # Automatically document code
    'sphinx.ext.napoleon',        # Support for Google style docstrings
    'sphinx.ext.viewcode',        # Add links to source code
    'sphinx.ext.todo',            # Manage to-do entries
    'sphinx.ext.intersphinx',     # Cross-referencing with other projects
    'sphinx_rtd_theme',           # Read the Docs theme
    'sphinx.ext.autosectionlabel',# Allow reference sections by title
    'sphinx.ext.autodoc.typehints', # Document type hints
    'sphinxcontrib.plantuml',     # PlantUML support
]

autodoc_default_options = {
    'members': True,
    'show-inheritance': True,
    'special-members': '__str__',
}

templates_path = ['_templates']
exclude_patterns = []
language = 'de'

# Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_logo = '_static/images/ris_logo.png'
html_favicon = '_static/images/favicon.ico'

html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]

# PlantUML configuration
plantuml_jar_path = os.path.abspath(os.path.join('..', '..', 'tools', 'plantuml.jar'))
plantuml = f'java -jar "{plantuml_jar_path}"'
plantuml_output_format = 'svg_obj'  # Generate both SVG and PNG formats

# Intersphinx configuration
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'django': ('https://docs.djangoproject.com/en/stable/', 'https://docs.djangoproject.com/en/stable/_objects/'),
}

# TODO extension settings
todo_include_todos = True

# EPUB options
epub_show_urls = 'footnote'

# Options for latex output
latex_elements = {
    'babel': '\\usepackage[ngerman]{babel}',
    'papersize': 'a4paper',
    'pointsize': '12pt',
    'preamble': r'''
        \usepackage[T1]{fontenc}
        \usepackage[utf8]{inputenc}
    ''',
}

latex_documents = [
    (
        'index',
        'RISBackendDokumentation.tex',
        'RIS Backend Dokumentation',
        'Maximiliano Santander',
        'manual'
    ),
]
