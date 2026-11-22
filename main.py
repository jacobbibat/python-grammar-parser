
from parser import (
    read_lexicon,
    read_rules,
    tokenize_sentence,
    get_pos_tags,
    parse
)


def main():
    print("AHLT Syntax Parser")
    print("------------------")

    lexicon = read_lexicon("lexicon.txt")
    categories, rules = read_rules("rules.txt")

    sentence = input("Enter a sentence: ")

    words = tokenize_sentence(sentence)
    pos_tags = get_pos_tags(words, lexicon)

    print("\nWords:", words)
    print("POS Tags:", pos_tags)

    tree = parse(words, pos_tags, rules)

    if tree is not None:
        print("\nSentence ACCEPTED")
        print("Root node:", tree.label)
        print("Root children:")

        for child in tree.children:
            print(child.label)
    else:
        print("\nSentence REJECTED")


if __name__ == "__main__":
    main()
