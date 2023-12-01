class Node:
    def __init__(self, label, symbols):
        self.label = label
        self.children = []
        self.parent = None
        self.symbols = symbols

    def setParent(self, parent):
        self.parent = parent

    def addChildren(self, children):
        self.children.extend(children)

    def __str__(self):
        return str(self.label)
        
class StateSpaceTree:
    def __init__(self, max_length, values, mode="sets"):
        self.root = Node([], values)
        self.nodes = [self.root]
        self.max_length = max_length
        self.mode = mode

    def expand(self, node):
        if len(node.label) == self.max_length:
            return []
        children = []
        for value in node.symbols:
            label = node.label + [value]
            child_values = node.symbols.copy()
            if self.mode == "perm no rep":
                child_values.remove(value)
            child = Node(label, child_values)
            child.setParent = node
            children.append(child)
        node.addChildren(children)
        self.nodes.extend(children)
        return children

    def get_leaves(self):
        leaves = []
        for node in self.nodes:
            if len(node.label) == self.max_length:
                leaves.append(node)
        return leaves