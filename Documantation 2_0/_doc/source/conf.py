# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# import
import os
import sys
import django

# Add project root to Python path
sys.path.insert(0, os.path.abspath('../..'))  # This points to ris_dev/

# Configure Django Settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ris_prj.settings.development')
django.setup()

project = 'RIS-Web Backend'
copyright = '2024, Maximiliano Santander'
author = 'Maximiliano Santander'
release = '1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx_rtd_theme',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinxcontrib.plantuml',
]

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []

# Language settings
language = 'en'
locale_dirs = ['locale/']
gettext_compact = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}

# PlantUML Configuration
plantuml_jar_path = os.path.abspath(os.path.join('..', '..', 'tools', 'plantuml.jar'))
plantuml = f'java -jar "{plantuml_jar_path}"'
plantuml_output_format = 'svg'

# Ensure PlantUML jar exists
if not os.path.exists(plantuml_jar_path):
    print(f"Warning: PlantUML jar not found at: {plantuml_jar_path}")
    print("Please run tools/download_plantuml.ps1 to download it")
    plantuml = None

