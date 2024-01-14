# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import datetime
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.abspath("../../"))

from inspect import getsourcefile

import python_template

# Get path to directory containing this file, conf.py.
DOCS_DIRECTORY = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))

# Set root logging level to INFO
import logging as logging_root

logger_root = logging_root.getLogger()
logger_root.setLevel(logging_root.INFO)


def ensure_pandoc_installed(_):
    import pypandoc

    # Download pandoc if necessary. If pandoc is already installed and on
    # the PATH, the installed version will be used. Otherwise, we will
    # download a copy of pandoc into docs/bin/ and add that to our PATH.
    pandoc_dir = os.path.join(DOCS_DIRECTORY, "bin")
    # Add dir containing pandoc binary to the PATH environment variable
    if pandoc_dir not in os.environ["PATH"].split(os.pathsep):
        os.environ["PATH"] += os.pathsep + pandoc_dir
    pypandoc.ensure_pandoc_installed(
        targetfolder=pandoc_dir,
        delete_installer=True,
    )


def setup(app):
    app.connect("builder-inited", ensure_pandoc_installed)


# -- Automatically generate JSON schema html pages -----------------------------
THIS_DIR = os.path.dirname(__file__)
BASE_DIR = Path(__file__).resolve().parents[2]


# -- General configuration ---------------------------------------------------

# General information about the project.
project = "python-template"
copyright = "%s, Louis Giron" % str(datetime.datetime.now().year)
author = "Louis Giron"
release = str(python_template.__version__)
version = release

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "nbsphinx",
    "autodocsumm",
    "sphinx.ext.napoleon",
    "sphinx_design",
    "IPython.sphinxext.ipython_directive",
    "IPython.sphinxext.ipython_console_highlighting",
    "sphinxcontrib.openapi",
]
autodoc_default_options = {
    "autosummary": False,
    "imported-members": True,
    "exclude-members": "Path",
    "undoc-members": True,
}

toc_object_entries = False
autoclass_content = "both"

# The master toctree document.
master_doc = "index"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_css_files = [
    "css/theme.css",
]

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
html_logo = "_static/python_template.png"

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
html_favicon = "_static/favicon-32x32.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Output file base name for HTML help builder.
htmlhelp_basename = "Lgiron-PythonTemplatedoc"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "pyarrow": ("https://arrow.apache.org/docs", None),
}

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

nbsphinx_custom_formats = {
    ".md": ["jupytext.reads", {"fmt": "mystnb"}],
}

nbsphinx_execute = os.environ.get("EXECUTE_DOC_NOTEBOOKS", "never")
