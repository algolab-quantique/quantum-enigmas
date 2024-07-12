# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Quantum Enigma"
copyright = "2024, AlgoLab"
author = "AlgoLab"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.githubpages",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.napoleon",
    "sphinx_mdinclude",
    "sphinx-thebe",
]


templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_logo = "_branding/logo.svg"
html_favicon = "_branding/favicon.png"
html_theme_options = {
    "repository_url": "https://github.com/algolab-quantique/pauliarray.git",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_download_button": False,
    "home_page_in_toc": True,
}
html_title = "PauliArray"


## supress typing warnings
nitpick_ignore = [("py:class", "type")]
