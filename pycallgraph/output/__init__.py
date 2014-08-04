try:
    from collections import OrderedDict
except ImportError as e:
    try:
        from ordereddict import OrderedDict
    except ImportError:
        raise ImportError("Cannot create OrderedDict instance")

from .output import Output
from .graphviz import GraphvizOutput
from .gephi import GephiOutput
from .ubigraph import UbigraphOutput
from .pickle import PickleOutput


outputters = OrderedDict([
    ('graphviz', GraphvizOutput),
    ('gephi', GephiOutput),
    # ('ubigraph', UbigraphOutput),
])
