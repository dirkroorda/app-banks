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

BASE_TYPE = "word"
CONDENSE_TYPE = "line"

NONE_VALUES = {None}

STANDARD_FEATURES = None  # meaning all loadable features

EXCLUDED_FEATURES = set()

NO_DESCEND_TYPES = {"lex"}

EXAMPLE_SECTION = "<code># Consider Phlebas</code>"
EXAMPLE_SECTION_TEXT = "# Consider Phlebas"

SECTION_SEP1 = " "
SECTION_SEP2 = ":"

WRITING = ""
WRITING_DIR = "ltr"

FONT_NAME = "Gentium"
FONT = "GentiumPlus-R.ttf"
FONTW = "GentiumPlus-R.woff"

TEXT_FORMATS = {}
TEXT_FORMATS = {
    "layout-orig-full": "layoutRich",
}

BROWSE_NAV_LEVEL = 2
BROWSE_CONTENT_PRETTY = False

VERSES = None

LEX = None

TRANSFORM = None

CHILD_TYPE = dict(book="chapter", chapter="sentence", sentence="word", line="word")

SUPER_TYPE = None

PLAIN_TYPES = None

PRETTY_TYPES = dict(
    book=("{title}", "author", ""),
    chapter=("{number}", "", ""),
    sentence=("{number}", "", ""),
    line=("{number}", "", "terminator"),
    word=(True, "", "gap"),
)

LEVELS = dict(
    book=dict(level=3, flow="col", wrap=False, stretch=False),
    chapter=dict(level=3, flow="col", wrap=False, strectch=False),
    sentence=dict(level=2, flow="col", wrap=False, strectch=True),
    line=dict(level=1, flow="row", wrap=True, strectch=True),
    word=dict(level=0, flow="col", wrap=False, strectch=False),
)

INTERFACE_DEFAULTS = dict(
    # withTypes=True,
    # withNodes=False,
    # showFeatures=True,
    # lineNumbers=None,
    # graphics=None,
)


def deliver():
    return (globals(), dirname(abspath(__file__)))
