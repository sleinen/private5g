# Copyright 2019-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os

def get_version():
    with open("VERSION") as f:
        return f.read().strip()

# -- Project information -----------------------------------------------------

project = u'5G Connectivity Service: A Systems Approach'
copyright = u'2019, 2020'
author = u'Larry Peterson, Oguz Sunay, and Bruce Davie'

# The short X.Y version
version = get_version()

# The full version, including alpha/beta/rc tags
release = get_version()

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# make all warnings errors
warning_is_error = True

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones. ***Replace "mathjax" with "imgmath" for epub output.***
extensions = [
    'sphinx.ext.coverage',
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinxcontrib.spelling',
    "sphinx_multiversion",
]

#extensions = [
#    'recommonmark',
#    'sphinx.ext.coverage',
#    'sphinx.ext.ifconfig',
#    'sphinx.ext.mathjax',
#    'sphinx.ext.todo',
#    'sphinx.ext.autosectionlabel',
#    'sphinxcontrib.actdiag',
#    'sphinxcontrib.blockdiag',
#    'sphinxcontrib.nwdiag',
#    'sphinxcontrib.packetdiag',
#    'sphinxcontrib.rackdiag',
#    'sphinxcontrib.seqdiag',
#]

# Text files with lists of words that shouldn't fail the spellchecker:
spelling_word_list_filename=['dict.txt', ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [u'_build', 'doc_venv', 'requirements.txt', 'Thumbs.db', '.DS_Store', 'repos', '*/vendor', 'sidebars', 'private', 'status.rst', '*/README.rst', 'CONTRIBUTING.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# Enable numbered figures
numfig = True
numfig_format = {
    'figure': 'Figure %s.',
    'table':  'Table %s.'
    }

# Ignore link check for the following websites
# linkcheck_ignore = [
#     'https://SDN.systemspproach.org/',
# ]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
  'prev_next_buttons_location': 'both'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# HTML Favicon
html_favicon = 'bridge.ico'

# HTML Index
html_use_index = False

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'SystemsApproach'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '11pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': 'private/latex/preamble.tex',

    # Latex figure (float) alignment
    #
    'figure_align': 'ht',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'book.tex', u'5G Connectivity Service: A Systems Approach',
     u'Peterson, Sunay, and Davie', 'manual', True),
]

latex_toplevel_sectioning = 'chapter'


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'Systems Approach', u'Systems Approach',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, '5G Connectivity Service', u'5G Connectivity Service',
     author, 'Peterson, Sunay, and Davie', 'A Systems Approach',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# blockdiag/etc. config

rackdiag_antialias = True
rackdiag_html_image_format = "SVG"
rackdiag_fontpath = [
    "_static/fonts/Inconsolata-Regular.ttf",
    "_static/fonts/Inconsolata-Bold.ttf",
]

nwdiag_antialias = True
nwdiag_html_image_format = "SVG"
nwdiag_fontpath = [
    "_static/fonts/Inconsolata-Regular.ttf",
    "_static/fonts/Inconsolata-Bold.ttf",
]

# -- Options for todo extension ----------------------------------------------
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Configure recommonmark to use AutoStructify -----------------------------
# Docs: https://recommonmark.readthedocs.io/en/latest/auto_structify.html

#import recommonmark
#from recommonmark.transform import AutoStructify

# -- Set up Google Analytics
# -- using approach at https://stackoverflow.com/questions/9444342/adding-a-javascript-script-tag-some-place-so-that-it-works-for-every-file-in-sph/41885884#41885884


GA_INVOKE_JS = """
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-C4RNJ35K6B');
"""

def setup(app):

    app.add_css_file('css/rtd_theme_mods.css')

    app.add_config_value('recommonmark_config', {
            'auto_toc_tree_section': 'Contents',
            }, True)

#    app.add_transform(AutoStructify)

    app.add_js_file('https://www.googletagmanager.com/gtag/js?id=G-C4RNJ35K6B')
    app.add_js_file(None, body=GA_INVOKE_JS)