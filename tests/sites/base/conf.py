# -- Project information -----------------------------------------------------

project = "Sphinx Book Theme"
copyright = "2020, Executable Book Project"
author = "Executable Book Project"

master_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["myst_nb", "sphinx_copybutton", "sphinx_togglebutton"]
html_theme = "sphinx_book_theme"
html_copy_source = True
html_sourcelink_suffix = ""
jupyter_execute_notebooks = "auto"

# Base options, we can add other key/vals later
html_theme_options = {
    "path_to_docs": "TESTPATH",
    "repository_url": "https://github.com/ExecutableBookProject/sphinx-book-theme",
    "repository_branch": "master",
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "jupyterhub_url": "https://datahub.berkeley.edu",
        "notebook_interface": "jupyterlab",
        "thebelab": True,
    },
}
