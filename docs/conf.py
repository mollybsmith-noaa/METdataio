# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys
sys.path.insert(0, os.path.abspath('.'))
print(sys.path)

# -- Project information -----------------------------------------------------

project = 'METdataio'
author = 'UCAR/NCAR, NOAA, CSU/CIRA, and CU/CIRES'
author_list = 'Hagerty, V., T. Burek, H. Fisher, and M. Win-Gildenmeister'
version = '2.0.0'
verinfo = version
release = f'{version}'
release_year = '2022'
release_date = f'{release_year}-06-22'
copyright = f'{release_year}, {author}'

# if set, adds "Last updated on " followed by
# the date in the specified format
html_last_updated_fmt = '%c'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc','sphinx.ext.intersphinx']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'Flowchart' ]

# Suppress certain warning messages
suppress_warnings = ['ref.citation']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes", ]
html_css_files = ['theme_override.css']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = os.path.join('_static','met_datadb_logo_2020_06.png')

# -- Intersphinx control -----------------------------------------------------
#intersphinx_mapping = {'numpy':("https://docs.scipy.org/doc/numpy/", None)}

numfig = True

numfig_format = {
    'figure': 'Figure %s',
}

# -- Export variables --------------------------------------------------------

rst_epilog = """
.. |copyright|    replace:: {copyrightstr}
.. |author_list|  replace:: {author_liststr}
.. |release_date| replace:: {release_datestr}
.. |release_year| replace:: {release_yearstr}
""".format(copyrightstr    = copyright,
           author_liststr  = author_list,
           release_datestr = release_date,
           release_yearstr = release_year)

