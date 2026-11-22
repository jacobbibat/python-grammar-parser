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