def get_hash(key):
    """
    Basic hash function that gets the mod(100) of the sum of ascii values of all
    the characters of the key string. This allows a maximum size of the hash to
    be 100 data objects.
    """
    s = 0  # sum of ascii
    for char in key:
        s += ord(char)
    return s % 100
