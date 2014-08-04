'''
Python Call Graph is a library and command line tool that visualises the flow
of your Python application.

See http://pycallgraph.slowchop.com/ for more information.
'''
try:
    "{}".format(1)
except ValueError:
    try:
        import stringformat
    except ImportError:
        raise ImportError(
            "Cannot use '{}' in a format statement! Add StringFormat!")
    else:
        stringformat.init(True)
except AttributeError:
    try:
        import stringformat
    except ImportError:
        raise ImportError(
            "Cannot use '{}' in a format statement! Add StringFormat!")
    else:
        stringformat.init()

from .metadata import __version__
from .metadata import __copyright__
from .metadata import __license__
from .metadata import __author__
from .metadata import __email__
from .metadata import __url__
from .metadata import __credits__

from .pycallgraph import PyCallGraph
from .exceptions import PyCallGraphException
from .config import Config
from .globbing_filter import GlobbingFilter
from .grouper import Grouper
from .util import Util
from .color import Color
from .color import ColorException
