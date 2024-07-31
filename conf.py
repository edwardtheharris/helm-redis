#!/usr/bin/env python3
"""Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""
# pylint: disable=invalid-name,redefined-builtin

from pathlib import Path
import version_query

def get_release():
    """Query the current release for the project."""
    repo_path = Path('.')
    ret_value = version_query.git_query.query_git_repo(repo_path).to_str()
    return ret_value

author = 'Xander Harris'
autoyaml_root = "."
autoyaml_doc_delimiter = "###"
autoyaml_comment = "#"
autoyaml_level = 10
autoyaml_safe_loader = True
copyright = '2024, Xander Harris'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.venv/*',
    '.tmp/*',
    '.pytest_cache/*',
]

extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.autoyaml',
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_logo = '_static/img/redis.png'
html_favicon = '_static/img/redis.png'
html_static_path = ['_static']
html_theme = 'sphinx_book_theme'
myst_dmath_double_inline=True
myst_enable_extensions = [
    "amsmath",
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_title_to_header = True
project = 'Redis Helm Chart'
rst_epilog = """
.. sectionauthor:: Xander Harris <xandertheharris@gmail.com>
"""
release = get_release()
show_authors=True
source_suffix = {
    '.md': 'markdown',
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
}
templates_path = ['_templates']
