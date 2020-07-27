class TreeNode:
    def __init__(self, data):
        """
        Initialises the attributes for each instance of the GeneralTree class.
        """
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        """
        Adds a child to the current node.
        """
        child.parent = self
        self.children.append(child)


def main():
    """
    Tests the TreeNode class.
    """
    root = TreeNode('Books')

    horror = TreeNode("Horror")
    horror.add_child(TreeNode("The Shining"))
    horror.add_child(TreeNode("1917"))
    horror.add_child(TreeNode("American Gods"))

    mystery = TreeNode("Mystery")
    mystery.add_child(TreeNode("Poirot"))
    mystery.add_child(TreeNode("Nancy Drew"))
    mystery.add_child(TreeNode("Girl on the Train"))

    emotive = TreeNode("Emotive")
    emotive.add_child(TreeNode('Normal People'))
    emotive.add_child(TreeNode('Abundance of Katherines'))
    emotive.add_child(TreeNode('Conversations with Friends'))

    root.add_child(mystery)
    root.add_child(horror)
    root.add_child(emotive)


if __name__ == "__main__":
    main()
