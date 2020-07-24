def make_anagrams(s1: str, s2: str) -> int:
    """
    Given 2 lowercase strings, how many chars would you have to remove in total
    to make the strings anagrams.
    For example:
    make_anagrams('hello','billion')
    >>> 6
    This is as you would have to remove 'h','e' from 'hello'- which is 2 letters
    and you would remove 'b','i','i','n' from 'billions' which is 4 characters.
    The remainig 'llo' and 'llo' are anagrams even if we shuffle them.
    """
