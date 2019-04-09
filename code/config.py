from os.path import dirname, abspath

PROTOCOL = 'http://'
HOST = 'localhost'
PORT = dict(
    kernel=19500,
    web=9500,
)

OPTIONS = ()

ORG = 'annotation'
REPO = 'banks'
CORPUS = 'Two quotes from Consider Phlebas by Iain M. Banks'
VERSION = '0.2'
RELATIVE = 'tf'

DOI_TEXT = '10.5281/zenodo.2630416'
DOI_URL = 'https://doi.org/10.5281/zenodo.2630416'

DOC_URL = (
    'https://nbviewer.jupyter.org/github/annotation/banks'
    '/blob/master/programs/convert.ipynb'
)
DOC_INTRO = ''
CHAR_URL = DOC_URL
CHAR_TEXT = 'How TF features represent text'

FEATURE_URL = DOC_URL

MODULE_SPECS = ()

ZIP = [REPO]

CONDENSE_TYPE = 'line'

NONE_VALUES = {None}

STANDARD_FEATURES = None  # meaning all loadable features

EXCLUDED_FEATURES = set()

NO_DESCEND_TYPES = {'lex'}

EXAMPLE_SECTION = '<code># Consider Phlebas</code>'
EXAMPLE_SECTION_TEXT = '# Consider Phlebas'

SECTION_SEP1 = ' '
SECTION_SEP2 = ':'

DEFAULT_CLS = 'txtn'
DEFAULT_CLS_ORIG = 'txtp'

FORMAT_CSS = dict(
    full='txtp',
    plain='txtp',
)

CLASS_NAMES = None

FONT_NAME = 'Gentium'
FONT = 'GentiumPlus-R.ttf'
FONTW = 'GentiumPlus-R.woff'

TEXT_FORMATS = {}
TEXT_FORMATS = {
    'layout-orig-full': 'layoutRich',
}


BROWSE_NAV_LEVEL = 2
BROWSE_CONTENT_PRETTY = False


def deliver():
  return (globals(), dirname(abspath(__file__)))
