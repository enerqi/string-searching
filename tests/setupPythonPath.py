# python2 & 3 compatibility
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type # make all classes new-style in python2

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
