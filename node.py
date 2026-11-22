class Node:

    def __init__(self, label, children=None):
        self.label = label

        if children is None:
            self.children = []
        else:
            self.children = children