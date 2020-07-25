class HashTable:
    def __init__(self):
        """
        Constructor that defines the maximum array size and initialises the
        array that is going to be used to store values for the hash table.
        """
        self.MAX = 100
        self.hash_arr = [None for _ in range(self.MAX)]

    def get_hash(self, key):
        """
        Basic hash function that gets the mod(100) of the sum of ascii values of all
        the characters of the key string. This allows a maximum size of the hash to
        be 100 data objects.
        """
        s = 0  # sum of ascii
        for char in key:
            s += ord(char)
        return s % 100
