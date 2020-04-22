from os.path import dirname, abspath

API_VERSION = 1

PROTOCOL = "http://"
HOST = "localhost"
PORT = dict(kernel=19500, web=9500)

ORG = "annotation"
REPO = "banks"
CORPUS = "Two quotes from Consider Phlebas by Iain M. Banks"
VERSION = "0.2"
RELATIVE = "tf"

DOI_TEXT = "10.5281/zenodo.2630416"
DOI_URL = "https://doi.org/10.5281/zenodo.2630416"

DOC_URL = (
    "https://nbviewer.jupyter.org/github/annotation/banks"
    "/blob/master/programs/convert.ipynb"
)
DOC_INTRO = ""
CHAR_URL = DOC_URL
CHAR_TEXT = "How TF features represent text"

FEATURE_URL = DOC_URL

MODULE_SPECS = ()

ZIP = [REPO]

EXAMPLE_SECTION = "<code># Consider Phlebas</code>"
EXAMPLE_SECTION_TEXT = "# Consider Phlebas"

DATA_DISPLAY = dict(
    noneValues={None},
    sectionSep1=" ",
    sectionSep2=":",
    writing="",
    writingDir="ltr",
    fontName="Gentium",
    font="GentiumPlus-R.ttf",
    fontw="GentiumPlus-R.woff",
    textFormats={"layout-orig-full": "layoutRich"},
    browseNavLevel=2,
    browseContentPretty=False,
)

TYPE_DISPLAY = dict(
    book=dict(
        template=True,
        featuresBare="author",
        children="chapter",
        level=3,
        flow="col",
        wrap=False,
        stretch=False,
    ),
    chapter=dict(
        template=True,
        children="sentence",
        level=3,
        flow="col",
        wrap=False,
        strectch=False,
    ),
    sentence=dict(
        template=True,
        children="word",
        level=2,
        flow="col",
        wrap=False,
        strectch=True,
    ),
    line=dict(
        template="{number}",
        features="terminator",
        children="word",
        verselike=True,
        condense=True,
        level=1,
        flow="row",
        wrap=True,
        strectch=True,
    ),
    word=dict(
        template=True,
        features="gap",
        base=True,
        level=0,
        flow="col",
        wrap=False,
        strectch=False,
    ),
)

INTERFACE_DEFAULTS = dict()


def deliver():
    return (globals(), dirname(abspath(__file__)))
