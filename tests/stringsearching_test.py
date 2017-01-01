# python2 & 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import (
         bytes, dict, int, list, object, range, str,
         ascii, chr, hex, input, next, oct, open,
         pow, round, super,
         filter, map, zip)

from hypothesis import given
from hypothesis.strategies import text
import pytest

from . import setupPythonPath
from stringsearching.naive import find_pattern_naive

__metaclass__ = type  # make all classes new-style in python2


def test_find_pattern_naive_raises_type_error_with_none_arguments():
    with pytest.raises(TypeError):
        find_pattern_naive(None, None)
    with pytest.raises(TypeError):
        find_pattern_naive(None, "string")
    with pytest.raises(TypeError):
        find_pattern_naive("pattern", None)


@given(text(), text())
def test_find_pattern_naive_only_gives_none_when_not_found(pattern, string):
    patternIndexInString = find_pattern_naive(pattern, string)

    # The system implementation functions as a correct alternative implementation for checking
    # whether the pattern exists in the string
    oracle_result = pattern in string

    assert patternIndexInString is not None if oracle_result else patternIndexInString is None


@given(text(), text())
def test_find_pattern_naive_gives_a_zero_based_index_for_found_patterns(pattern, string):
    patternIndexInString = find_pattern_naive(pattern, string)

    oracle_result = string.find(pattern)

    if oracle_result == -1:
        assert patternIndexInString is None
    else:
        assert oracle_result == patternIndexInString
