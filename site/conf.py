# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

html_theme = 'alabaster'


project = '6. Sınıf Ders Notları'
copyright = 'Blog 2023'
author = 'karahan'
language = 'tr'
extensions = ['sphinx.ext.autodoc', 'rst2pdf.pdfbuilder']
smartquotes = False

# -- Options for PDF output --

pdf_documents = [('index', u'rst2pdf', u'Bilişim Teknolojileri ve Yazılım Dersi', u'BTY 6. Sınıf'),]
pdf_stylesheets = ['style-main.yaml', 'tango']
pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']
pdf_style_path = [ '.', 'site/_static']
pdf_use_coverpage = True
pdf_use_toc = True
pdf_default_dpi = 96
pdf_compressed = True
pdf_language = "tr_TR"
pdf_fit_mode = "shrink"
pdf_use_unicodesubset = False

# -- Options for HTML output --

html_baseurl = 'https://bayramkarahan.github.io/'
#html_theme = 'alabaster'


html_static_path = ['_static']
html_theme_options = {
    'font_family' : 'monospace',
    'footnote_bg': 'none',
    'page_width': '100%',
    'body_max_width': 'auto',
    'logo': 'logo.svg',

}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
    ]
}
