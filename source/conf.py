# -- Project information -----------------------------------------------------

project = 'bolivar.ooo'
copyright = '2020, Martí Bolívar'
author = 'Martí Bolívar'

# -- General configuration ---------------------------------------------------

extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

html_theme_options = {
    'show_powered_by': False,
    'show_relbars': False,
}

html_show_sourcelink = False

html_copy_source = False

html_sidebars = {
    '**': [
        'about.html',
        'searchbox.html',
    ]
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
