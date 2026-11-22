
from parser import*

def main():
    print("AHLT Syntax Parser")
    print("------------------")

    lexicon = read_lexicon("lexicon.txt")
    categories, rules = read_rules("rules.txt")

    sentence = input("Enter a sentence: ")

    words = tokenize_sentence(sentence)
    pos_tags = get_pos_tags(words, lexicon)

    print("\nWords: ", words)
    print("POS TAGS: ", pos_tags)


            
if __name__ == "__main__":
    main()
