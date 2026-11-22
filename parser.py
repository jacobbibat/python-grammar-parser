
from node import Node

def read_lexicon(filename):
    lexicon = {}

    with open(filename, "r", encoding="utf-8") as file:
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

            if len(parts) >= 2:
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

    def reduce(nodes):
        labels = []

        for node in nodes:
            labels.append(node.label)

        print("Current:", labels)

        if labels == ["S"]:
            return nodes

        for start in range(len(nodes)):
            for end in range(start + 1, len(nodes) + 1):
                selected = nodes[start:end]

                tags = []

                for node in selected:
                    tags.append(node.label)

                    parent = find_matching_rule(tags, rules)

                    if parent is not None:
                        new_node = Node(parent, selected)

                        nodes = (
                            nodes[:start]
                            + [new_node]
                            + nodes[end:]
                        )

                        return reduce(nodes)

        return nodes

    return reduce(nodes)


def check_agreement(words, pos_tags, lexicon):
    subject_number = None
    verb_number = None

    for i in range(len(pos_tags)):

        if pos_tags[i] in ["NN", "NNS"] and subject_number is None:
            subject_number = lexicon[words[i]]["number"]

        if pos_tags[i] in ["VBZ", "VBP"] and verb_number is None:
            verb_number = lexicon[words[i]]["number"]

    if subject_number is None or verb_number is None:
        return False

    return subject_number == verb_number
