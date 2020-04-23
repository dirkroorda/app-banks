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

DATA_DISPLAY = dict(textFormats={"layout-orig-full": "layoutRich"},)

TYPE_DISPLAY = dict(
    book=dict(featuresBare="author",),
    sentence=dict(flow="col",),
    line=dict(template="{number}", features="terminator", verselike=True,),
    word=dict(features="gap",),
)

INTERFACE_DEFAULTS = dict()


def deliver():
    return (globals(), dirname(abspath(__file__)))
