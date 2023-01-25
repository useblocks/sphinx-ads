from docutils.parsers.rst import Directive, directives
from sphinx.errors import SphinxError


class AdsDirectiveException(SphinxError):
    pass


class AdsDirective(Directive):
    final_argument_whitespace = True
    option_spec = {
        "types": directives.unchanged,
        "links": directives.unchanged,
        "options": directives.unchanged,
        "usage": directives.unchanged,
    }
