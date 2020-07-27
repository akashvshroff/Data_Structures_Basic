class GeneralTree:
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
