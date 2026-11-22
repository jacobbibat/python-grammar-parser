from parser import *

lexicon = read_lexicon("lexicon.txt")
categories, rules = read_rules("rules.txt")

sentence = input("Enter a sentence: ")

words = tokenize_sentence(sentence)
pos_tags = get_pos_tags(words, lexicon)

# Parse the sentence
nodes = parse(words, pos_tags, rules)

# Check grammar and subject-verb agreement
if len(nodes) == 1 and nodes[0].label == "S" and check_agreement(words, pos_tags, lexicon):
    print("\nSentence ACCEPTED")
else:
    print("\nSentence REJECTED")

# Display bracketed structure
print("\nBracketed Structure:")

for node in nodes:
    print(node.to_brackets())

# Display syntax tree
print("\nSyntax Tree:")

for node in nodes:
    node.print_tree()