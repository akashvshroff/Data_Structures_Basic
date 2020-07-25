class HashTable:
    def __init__(self):
        """
        Constructor that defines the maximum array size and initialises the
        array that is going to be used to store values for the hash table.
        """
        self.MAX = 100
        self.hash_arr = [[] for _ in range(self.MAX)]

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
        Accepts a key value pair to add into the hashmap. If exists, then the
        value is updated, otherwise appended to the end of the list.
        """
        found = False
        ind = self.get_hash(key)  # index for key
        for idx, element in enumerate(self.hash_arr[ind]):
            if element[0] == key and len(element) == 2:
                self.hash_arr[ind][idx] = (key, val)
                found = True
                break
        if not found:
            self.hash_arr[ind].append((key, val))

    def __getitem__(self, key):
        """
        Retrieves a value based on key, iterates over all possible stored key,
        values at the index in case of collision.
        """
        ind = self.get_hash(key)
        arr = self.hash_arr[ind]
        for k, v in arr:
            if k == key:
                return v

    def __delitem__(self, key):
        """
        Deletes an item at a particular key.
        """
        ind = self.get_hash(key)
        arr = self.hash_arr[ind]
        for idx, (k, v) in enumerate(arr):
            if k == key:
                del self.hash_arr[ind][idx]


def main():
    """
    Controls hashtable through an object.
    """
    hash = HashTable()
    hash['foo'] = 25
    hash['fii'] = 65
    hash['bar'] = 80
    hash['boo'] = 38
    hash['bam'] = 89

    print(hash['bam'])
    del hash['bam']
    print(hash['foo'])
    print(hash['bam'])


if __name__ == '__main__':
    main()
