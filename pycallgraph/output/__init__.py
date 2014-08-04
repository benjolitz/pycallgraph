try:
    from collections import OrderedDict
except ImportError as e:
    try:
        import ordereddict as OrderedDict
    except ImportError:
        raise e

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
