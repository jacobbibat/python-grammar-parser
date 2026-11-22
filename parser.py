from node import Node

def read_lexicon(filename):
    lexicon = {}

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()

            if len(parts) == 4:
                word, pos, root, number = parts

                lexicon[word.lower()] = {
                    "pos": pos,
                    "root": root,
                    "number": number
                }

        return lexicon

def read_rules(filename):
    rules = {}

    with open(filename, "r", encoding="utf-8") as file:
        categories = file.readline().strip().split()

        for line in file:
            parts = line.strip().split()

            if len(parts) >=2:
                parent = parts[0]
                children = parts[1:]

                if parent not in rules:
                    rules[parent] = []

                rules[parent].append(children)

    return categories, rules

def tokenize_sentence(sentence):
    words = sentence.lower().split()
    return words

def get_pos_tags(words, lexicon):
    pos_tags = []

    for word in words:
        if word in lexicon:
            pos_tags.append(lexicon[word]["pos"])
        else:
            pos_tags.append("UNKNOWN")

    return pos_tags

def find_matching_rule(sequence, rules):

    for parent, productions in rules.items():

        for children in productions:

            if sequence == children:
                return parent

    return None




def parse(words, pos_tags, rules):

    nodes = []

    for word, pos in zip(words, pos_tags):
        word_node = Node(word)
        pos_node = Node(pos, [word_node])
        nodes.append(pos_node)

    def try_reductions(current):

        if len(current) == 1 and current[0].label == "S":
            return current[0]

        for start in range(len(current)):

            for end in range(start + 1, len(current) + 1):

                selected_nodes = current[start:end]

                sequence = [
                    node.label for node in selected_nodes
                ]

                for parent, productions in rules.items():

                    for children in productions:

                        if sequence == children:

                            parent_node = Node(
                                parent,
                                selected_nodes
                            )

                            new_sequence = (
                                current[:start]
                                + [parent_node]
                                + current[end:]
                            )

                            result = try_reductions(new_sequence)

                            if result is not None:
                                return result

        return None

    return try_reductions(nodes)


