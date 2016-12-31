# python2 & 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import (
         bytes, dict, int, list, object, range, str,
         ascii, chr, hex, input, next, oct, open,
         pow, round, super,
         filter, map, zip)
__metaclass__ = type # make all classes new-style in python2

from . import setupPythonPath

def test_hey():
    greet =  "Hey " + "you"
    assert greet == "Hey you"

