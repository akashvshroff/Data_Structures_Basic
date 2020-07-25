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

    def __setitem__(self, key, val):
        """
        Accepts a key value pair to add into the hashmap.
        """
        ind = self.get_hash(key)  # index for key
        self.hash_arr[ind] = val  # stores value - to add, collision handling.

    def __getitem__(self, key):
        """
        Retrieves a value based on key.
        """
        ind = self.get_hash(key)
        return self.hash_arr[ind]

    def __delitem__(self, key):
        """
        Deletes an item at a particular key.
        """
        ind = self.get_hash(key)
        self.hash_arr[ind] = None


def main():
    """
    Controls hashtable through an object.
    """
    hash = HashTable()


if __name__ == '__main__':
    main()
