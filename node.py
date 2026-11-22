class Node:

    def __init__(self, label, children=None):
        self.label = label

        if children is None:
            self.children = []
        else:
            self.children = children

    def to_brackets(self):

        if not self.children:
            return self.label

        child_brackets = []

        for child in self.children:
            child_brackets.append(child.to_brackets())

        return "[" + self.label + " " + " ".join(child_brackets) + "]"

    
    def print_tree(self):

        print(self.label)

        def print_children(node, prefix):

            for index, child in enumerate(node.children):

                is_last = index == len(node.children) - 1

                connector = "└── " if is_last else "├── "

                print(prefix + connector + child.label)

                new_prefix = prefix + (
                    "    " if is_last else "│   "
                )

                print_children(child, new_prefix)

        print_children(self, "")
