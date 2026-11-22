from parser import*

def main():
    categories, rules = read_rules("rules.txt")

    print("AHLT Grammar Matching Test")
    print("--------------------------")

    test_sequences = [
        ["DT", "NN"],
        ["DT", "JJ", "NN"],
        ["VBZ", "NP"],
        ["NP", "VP"],
        ["NN", "DT"],
    ]

    for i in test_sequences:
        result = find_matching_rule(i, rules)

        print(i, "->", result)

            
if __name__ == "__main__":
    main()
