# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# imports
import os
import sys
sys.path.insert(0, os.path.abspath('../../..'))


# Project information
project = 'RIS Backend Documentation'
copyright = '2024, RIS Development'
author = 'Maximiliano Santander'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',          # API documentation
    'sphinx.ext.napoleon',         # Google/NumPy style docstrings
    'sphinx.ext.viewcode',         # Add links to source code
    'sphinx.ext.graphviz',         # Diagram support
    'sphinx.ext.intersphinx',      # Link to other projects
    'sphinx.ext.todo',             # Todo notes
    'sphinx.ext.autosectionlabel', # Reference sections by name
]

# Napoleon settings for docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_rtype = True

# Language settings
language = 'de'
locale_dirs = ['locale/']
gettext_compact = False

# HTML output options
html_theme = 'sphinx_rtd_theme'    # ReadTheDocs theme
html_static_path = ['_static']
html_logo = '_static/images/ris_logo.svg'
html_favicon = '_static/images/favicon.ico'

# Additional options
templates_path = ['_templates']
exclude_patterns = []
source_suffix = '.rst'
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


