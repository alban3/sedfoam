import re

DOXYFILE = 'Doxyfile-mcss'

STYLESHEETS = [
    'https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600&subset=latin-ext',
    '../css/m-dark+documentation.compiled.css'
]

MAIN_PROJECT_URL = 'https://github.com/SedFoam/sedfoam'

LINKS_NAVBAR1 = [
    (None, 'pages', [
        ("<a href=\"index.html\">About sedFoam</a>",),
        (None, 'install'),
        (None, 'howtodocker'),
        (None, 'howtogit'),
        (None, 'faq'),
        ("Publications", 'publicationList')
    ]),
    ('Tutorials', 'pages', [
        ("Laminar flow Tutorials", 'tutorials_laminar'),
        ("Turbulence-averaged flow tutorials", 'tutorials_RAS'),
        ("Turbulence-resolving flow tutorials", 'tutorials_LES'),
        ("Non-dimensional solution", 'ndsolution'),
        ("Dynamic mesh tutorials", 'tutorials_DyM'),
        ("Input description", 'inputs')
    ])
]
LINKS_NAVBAR2 = [
    ('Model', 'governingEq', [
        ("Governing equations", 'governingEq'),
        ("Algorithm", 'algoSedFoam')
    ]),
    (None, 'annotated', []),
    (None, 'files', [])
]

FINE_PRINT = """<p>sedFoam docs. Part of the <a href="https://github.com/SedFoam/sedfoam">sedFoam project</a>, copyright © <a href="cyrille.bonamy@univ-grenoble-alpes.fr/">Cyrille Bonamy</a> and <a href="credits-contributors.html">contributors</a>, 2015&ndash;2021.<br />Generated by <a href="https://doxygen.org/">Doxygen</a> {doxygen_version} and <a href="https://mcss.mosra.cz/">m.css</a>. Contact the team via <a href="https://github.com/SedFoam/sedfoam">GitHub</a>, <a href="mailto:cyrille.bonamy@univ-grenoble-alpes.fr">e-mail</a> or <a href="https://twitter.com/sedfoam">Twitter</a>.</p>"""

SEARCH_HELP = """<p class="m-noindent">Search for symbols, directories, files, pages, OpenGL, GLSL, Vulkan and OpenAL APIs. You can omit any prefix from the symbol or file path; adding a <code>:</code> or <code>/</code> suffix lists all members of given symbol or directory.</p> <p class="m-noindent">Use <span class="m-label m-dim">&darr;</span> / <span class="m-label m-dim">&uarr;</span> to navigate through the list, <span class="m-label m-dim">Enter</span> to go. <span class="m-label m-dim">Tab</span> autocompletes common prefix, you can copy a link to the result using <span class="m-label m-dim">⌘</span> <span class="m-label m-dim">L</span> while <span class="m-label m-dim">⌘</span> <span class="m-label m-dim">M</span> produces a Markdown link.</p>"""

FAVICON = 'sedFoam_favicon.png'

VERSION_LABELS = True

_magnum_colors_src = re.compile(r"""<span class="mh">0x(?P<hex>[0-9a-f]{6})(?P<alpha>[0-9a-f]{2})?(?P<literal>_s?rgba?f?)</span>""")
_magnum_colors_dst = r"""<span class="mh">0x\g<hex>\g<alpha>\g<literal><span class="m-code-color" style="background-color: #\g<hex>;"></span></span>"""

# Code wrapped in DOXYGEN_IGNORE() will get replaced by an (Unicode) ellipsis
# in the output. In order to make the same code compilable, add
#
#   #define DOXYGEN_IGNORE(...) __VA_ARGS__
#
# to the snippet code
def _doxygen_ignore(code: str):
    while 'DOXYGEN_IGNORE(' in code:
        i = code.index('DOXYGEN_IGNORE(')
        depth = 1
        for j in range(i + len('DOXYGEN_IGNORE('), len(code)):
            if code[j] == '(': depth += 1
            elif code[j] == ')': depth -= 1
            if depth == 0: break
        assert depth == 0, "unmatched DOXYGEN_IGNORE() parentheses in %s" % code
        code = code[:i] + '…' + code[j+1:]
    return code

M_CODE_FILTERS_PRE = {
    'C++': _doxygen_ignore
}

M_CODE_FILTERS_POST = {
    'C++': lambda str: _magnum_colors_src.sub(_magnum_colors_dst, str)
}
