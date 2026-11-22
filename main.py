
from parser import*

def main():
    print("AHLT Syntax Parser")
    print("------------------")

    lexicon = read_lexicon("lexicon.txt")
    categories, rules = read_rules("rules.txt")


    print("Lexicon loaded successfully!")
    print("Total words:", len(lexicon))

    word = input("Enter a word: ").lower()

    if word in lexicon:
        print("Word found!")
        print("Information:", lexicon[word])

    else:
        print("Word not found in lexicon")

    print("###################################")

    print("categories:", categories)

    print ("\nGrammar rules:")

    for parent, productions in rules.items():
        for children in productions:
            print(parent, "->", " ".join(children))

            
if __name__ == "__main__":
    main()
