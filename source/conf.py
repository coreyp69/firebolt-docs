# -*- coding: utf-8 -*-
#
# symbol-docs documentation build configuration file, created by
# sphinx-quickstart on Mon Dec 18 16:39:26 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('_ext'))
import sphinx_bootstrap_theme


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.githubpages',
    'sphinx.ext.ifconfig',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'examplecode',
    'sphinxcontrib.mermaid',
    'sphinxcontrib.viewsource',
    'sphinxcontrib.ghcontributors',
    'sphinx_tabs.tabs',
    'ablog',
    'edit-on-github',
    'fulltoc',
    'ghreference',
    'redirects',
    'm2r2', # To support direct rendering of MarkDown files
    'gitstamp',
    'serializationref',
    'card',
]

# Add any paths that contain templates here, relative to this directory.
import ablog
templates_path = ['_templates']
templates_path.append(ablog.get_html_templates_path())

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.md']

# The main toctree document.
master_doc = 'index'

# General information about the project.
project = u'symbol-docs'
copyright = u'2018-present, NEM'
author = u'NEM'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'0.22.2'

# The full version, including alpha/beta/rc tags.
release = u'Main'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

locale_dirs = ['locale/']
gettext_compact = False

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['**/node_modules']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'inkpot'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#

html_theme_options = {
    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Site",

    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': False,

    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': False,

    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "Page",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 2,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "true",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "exclude",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing (default) or the name of a valid theme
    # such as "cosmo" or "sandstone".
    #
    # The set of valid themes depend on the version of Bootstrap
    # that's used (the next config option).
    #
    # Currently, the supported themes are:
    # - Bootstrap 2: https://bootswatch.com/2
    # - Bootstrap 3: https://bootswatch.com/3
    'bootswatch_theme': "cosmo",

    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    'bootstrap_version': "3",
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "resources/images/firebolt-logo.svg"

# Docs Title
html_title = 'Firebolt Documentation'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', 'resources/scripts']

# Additional html pages
html_additional_pages = {'404': '404.html'}

## Custom style overrides
def setup(app):
    app.add_css_file("https://use.fontawesome.com/releases/v5.2.0/css/all.css")
    app.add_css_file("css/custom.css")  # may also be an URL
    app.add_js_file("js/custom.js")

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
html_sidebars = {
  '**': ['globaltoc.html'],
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'symbol-docs'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'symbol-docs.tex', u'Symbol Documentation',
     u'nem', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'symbol-docs', u'Symbol Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'symbol-docs', u'Symbol Documentation',
     author, 'symbol-docs', 'One line description of project.',
     'Miscellaneous'),
]

# -- Options for substitutions --

rst_prolog = """
.. |codename| replace:: Symbol
.. |sitename| replace:: Symbol Developer Documentation
.. |networkcurrency| replace:: ``symbol.xym``
.. |privatenetworkcurrency| replace:: ``cat.currency``
.. |sdk| replace:: Symbol SDK
.. |cli| replace:: Symbol CLI
.. |desktop-wallet| replace:: Symbol Desktop Wallet
.. |discord| raw:: html

   <a href="https://discord.com/invite/xymcity" target="_blank">Discord</a>

.. |nem| raw:: html

    <a href="https://nem.io/" target="_blank">NEM</a>

.. |twitter| raw:: html

   <a href="https://twitter.com/NEMofficial" target="_blank">Twitter</a>

.. |github| raw:: html

   <a href="https://github.com/symbol" target="_blank">GitHub</a>

.. |symbol-bootstrap| raw:: html

   <a href="https://github.com/fboucquez/symbol-bootstrap" target="_blank">Symbol Bootstrap</a>

.. |techref| raw:: html

   <a href="https://docs.symbolplatform.com/symbol-technicalref/main.pdf" target="_blank">Technical Reference</a>
"""

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html, references.html, guides.html']


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

html_favicon = 'favicon.ico'

# -- Options for edit on github -------------------------------------------

edit_on_github_project = 'symbol/symbol-docs'
edit_on_github_branch = 'main'

# -- Options for edit scaled images ---------------------------------------

html_scaled_image_link = False

# -- Options for ablog ----------------------------------------------------
blog_baseurl = '/'
blog_path = 'guides'

blog_authors = {}

# -- Options for linkcheck ------------------------------------------------

linkcheck_ignore = [
    r'http://localhost',
    r'https://localhost',
    r'https://my-symbol-node.com',
    r'https://symbol.github.io/symbol-openapi/[^/]*/#', # Dynamic page
    r'.*\.ts', r'.*\.js', r'.*\.java', r'.*\.cats', # Too many of them, GitHub complains
    r'https://nemplatform.com/.*#', r'https://forum.nem.io', # DDoS protection delays serving the real page
    r'https://twitter.com/', # Returns 400 Client Error: Bad Request for url
    r'/_images/.*', # Ignore image targets, linkcheck does not know they will be deployed
    r'/_static/.*', # Ignore things we put there manually, linkcheck does not know they will be deployed
    r'/guides/.*', # Mysterious autogenerated page, not available at linkcheck time
    r'https://hackmd.io/.*', # You need to login to access some of the pages
]
linkcheck_anchors_ignore = [r'L\d+']

# -- Options for viewsource ------------------------------------------------
viewsource_title = 'View Code'

# -- Options for m2r2 ------------------------------------------------------
m2r_anonymous_references = True # Otherwise we get duplicated link names

def viewsource_resolve_link(file_path, language=None):
    if language == 'javascript':
        language = 'typescript'
    if language == 'java':
        language = 'java/src/test/java/symbol/guides/examples'
    base_url = 'https://github.com/symbol/symbol-docs/blob/main/source/resources/examples/%s/' % language
    path_split = file_path.split('/')
    path = "/".join(path_split[len(path_split)-2:])
    return base_url + path

# -- Custom extlinks -----------------------------------------------------

extlinks = {'schema': ('https://github.com/symbol/blob/main/catbuffer/schemas/symbol/%s', 'file '),
            'properties': ('https://github.com/symbol/symbol/blob/main/client/catapult/resources/%s', 'file ')}

# -- Custom Pygments lexers ----------------------------------------------

from pygments.lexers.shell import BashLexer
from pygments import token
from sphinx.highlighting import lexers

# These are just plain Bash lexers with different names, so we can have tabbed code snippets
# with custom names on the tabs, instead of just the language code.
# If we ever feel like it, we can add custom coloring:
# https://stackoverflow.com/questions/16469869/custom-syntax-highlighting-with-sphinx

class CatapultLexer(BashLexer):
    name = 'catapult-client'

lexers['catapult-client'] = CatapultLexer()

class CliLexer(BashLexer):
    name = 'symbol-cli'

    tokens = {
        'root': [
            (r'^\? ', token.Keyword), # Blue, with the inkpot style
            (r'(^SUCCESS |^✔ )', token.Generic.Inserted),  # Green
            (r'^ERR ', token.Name.Exception),  # Red
            (r'(Account|Property|Value)', token.Comment.Preproc), # Blue
            (r'.', token.Text)
        ]
    }

lexers['symbol-cli'] = CliLexer()

class BootstrapLexer(BashLexer):
    name = 'symbol-bootstrap'

    tokens = {
        'root': [
            (r'^\? ', token.Generic.Inserted), # Green, with the inkpot style
            (r'^info ', token.Generic.Inserted), # Green
            (r'^error ', token.Name.Exception), # Red
            (r'.', token.Text)
        ]
    }

lexers['symbol-bootstrap'] = BootstrapLexer()

user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0'
