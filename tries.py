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

    def search(self, word):
        """
        Search for a whole word in the trie.
        """
        if not self.root.children:
            print("Error: No words in the trie.")
            return
        cur = self.root
        for letter in word:
            if letter in cur.children:
                cur = cur.children[letter]
            else:
                return False
        if cur.is_complete:
            return True
        else:
            return False

    def starts_with(self, word):
        """
        Checks if a word stored in the trie starts with the word inputted.
        """
        if not self.root.children:
            print("Error: No words in the trie.")
            return
        cur = self.root
        for letter in word:
            if letter in cur.children:
                cur = cur.children[letter]
            else:
                return False
        return True

    def remove(self, word):
        """
        Removes a user inputted word from the trie if whole word exists in trie.
        """
        if not self.root.children:
            print("Error: No words in the trie.")
            return
        if not self.search(word):
            print("Error: word not found in trie.")
            return
        cur = self.root
        for letter in word:
            cur = cur.children[letter]
        cur.is_complete = False

    def show_trie(self, node, level=0, letter=''):
        """
        Display the trie prettily.
        """
        indent = ''
        if level > 1:
            num = 1*level-1
            indent = ' '*num+'|_'
        mark = '*' if node.is_complete else ''
        print(f'{indent} {letter} {mark}')
        if not node.children:
            return
        for letter, child in node.children.items():
            level += 1
            self.show_trie(child, level, letter)
            level -= 1


def main():
    """
    Creates a trie and inputs data to ensure class is working.
    """
    trie = Trie()
    trie.add('cards')
    trie.add('trie')
    trie.add('try')
    trie.add('card')
    trie.add('cot')
    trie.add('cots')
    print(trie.search('try'))
    print(trie.search('tried'))
    trie.remove('try')
    print(trie.search('try'))
    print(trie.starts_with('cot'))
    trie.show_trie(trie.root)


if __name__ == '__main__':
    main()
