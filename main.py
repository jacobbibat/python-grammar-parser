
from parser import*

def main():
    print("AHLT Syntax Parser")
    print("------------------")

    lexicon = read_lexicon("lexicon.txt")


    print("Lexicon loaded successfully!")
    print("Total words:", len(lexicon))

    word = input("Enter a word: ").lower()

    if word in lexicon:
        print("Word found!")
        print("Information:", lexicon[word])

    else:
        print("Word not found in lexicon")

if __name__ == "__main__":
    main()
