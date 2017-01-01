
def find_pattern_naive(pattern, string):
    """Return the starting index of pattern in string or None if it is not found.

    Attempts to find a single pattern (substring) within a string.
    Complexity O(|Text| * |Pattern|)

    This will actually work with lists of equatable objects, not just strings.
    """
    # None arguments are invalid
    if pattern is None or string is None:
        raise TypeError("arguments must not be None")

    # The empty pattern "" matches all inputs
    if not pattern:
        return 0

    lastStringIndex = len(string) - 1
    lastPatternIndex = len(pattern) - 1

    # When the pattern is longer than the input string no match is possible
    if lastPatternIndex > lastStringIndex:
        return None

    for index in range(len(string)):

        for patternIndex, patternChar in enumerate(pattern):

            strIndex = index + patternIndex
            if strIndex > lastStringIndex:
                # This is arguably a bit more optimized than pure brute force
                return None

            if string[strIndex] != patternChar:
                # pattern not matched from char `index` of string, continue walking the string
                break

            if patternIndex == lastPatternIndex:
                # the last character of the pattern matched so found substring
                return index
