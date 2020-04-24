from os.path import dirname, abspath

API_VERSION = 1

PROVENANCE_SPEC = dict(
    org="annotation",
    repo="banks",
    version="0.2",
    doi="10.5281/zenodo.2630416",
    corpus="Two quotes from Consider Phlebas by Iain M. Banks",
)

DOCS = dict(
    docExt=".ipynb",
    docRoot="{urlNb}",
    docBase="{docRoot}/{org}/{repo}/blob/master/programs",
    docPage="convert",
    featureBase="{docBase}",
    featurePage="convert",
)

DATA_DISPLAY = dict(textFormats={"layout-orig-full": "layoutRich"})

TYPE_DISPLAY = dict(
    book=dict(featuresBare="author"),
    sentence=dict(flow="col"),
    line=dict(template="{number}", features="terminator", verselike=True),
    word=dict(features="gap"),
)

INTERFACE_DEFAULTS = dict()


def deliver():
    return (globals(), dirname(abspath(__file__)))
