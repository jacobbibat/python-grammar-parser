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