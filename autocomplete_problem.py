class TrieNode:
    def __init__(self):
        """
        Initialises a node of the trie and stores some basic information in it.
        """
        self.children = {}
        self.is_complete = None


class Trie:
    def __init__(self):
        """
        Initialises a default root node.
        """
        self.root = TrieNode()

    def add(self, word):
        """
        Add a word to the trie.
        """
        cur = self.root
        word_length = len(word)
        for idx, letter in enumerate(word):
            if letter in cur.children:
                cur = cur.children[letter]
            else:
                cur.children[letter] = TrieNode()
                cur = cur.children[letter]
            if idx == word_length - 1:  # last letter
                cur.is_complete = True

    def get_by_query(self, query):
        """
        Returns a list of all the possible words by a given query.
        """
        if not self.root.children:
            print("Error: Empty Trie")
            return []
        cur = self.root
        for letter in query:
            if letter in cur.children:
                cur = cur.children[letter]
            else:
                print("Error: No matches.")
                return []
        # Now cur.children has all the possible matches.
        found = []
        prefix = query
        stack = [(cur, prefix)]
        while stack:
            """
            A stack of all the possible words get built in a BFS approach that
            ultimately pops the word once it is finished. If it isn't finished,
            the word is appended back onto the stack and the process continues.
            """
            cur, prefix = stack.pop()
            if cur.is_complete:
                found.append(prefix)
            for letter, node in cur.children.items():
                stack.append((node, prefix+letter))
        return found


def get_suggestions(words, query):
    """
    Implement an autocomplete system. That is, given a query string s and a set
    of all possible query strings, return all strings in the set that have s as
    a prefix.
    For example, given the query string de and the set of strings
    [dog, deer, deal], return [deer, deal].
    Hint: Try preprocessing the dictionary into a more efficient data
    structure to speed up queries.

    Method: Preprocess all data into a trie and then recursively generate all
    words that have the prefix.
    """
    trie = Trie()
    for word in words:
        trie.add(word)
    res = trie.get_by_query(query)
    return res


print(get_suggestions(['dog', 'dear', 'deal'], 'de'))
