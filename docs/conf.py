import os
import sys

# Add the path to your module to sys.path
sys.path.insert(0, os.path.abspath('../src'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Template'
copyright = 'CC BY-NC-SA 4.0'
author = "Firstname 'Nickname' SURNAME <email>"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinxcontrib.mermaid',
              'sphinx.ext.napoleon',
              "sphinx_rtd_theme",
              'enum_tools.autoenum']
autodoc_typehints = 'none'  # do not add type annotations
templates_path = ['_templates']
exclude_patterns = []
autodoc_preserve_defaults = False
language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
  'collapse_navigation': False,
  'sticky_navigation': True,
  'navigation_depth': 4,
}
html_css_files = [
  'custom.css',
]
html_static_path = ['_static']
