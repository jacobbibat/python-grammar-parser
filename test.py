
import unittest
from parser import *


class TestParser(unittest.TestCase):

    def setUp(self):
        self.lexicon = read_lexicon("lexicon.txt")
        self.categories, self.rules = read_rules("rules.txt")

    def test_read_lexicon(self):
        self.assertEqual(self.lexicon["man"]["pos"], "NN")

    def test_read_rules(self):
        self.assertIn(["NP", "VP"], self.rules["S"])

    def test_tokenize_sentence(self):
        words = tokenize_sentence("The Man Likes")
        self.assertEqual(words, ["the", "man", "likes"])

    def test_get_pos_tags(self):
        words = ["the", "man", "likes"]
        pos_tags = get_pos_tags(words, self.lexicon)
        self.assertEqual(pos_tags, ["DT", "NN", "VBZ"])

    def test_find_matching_rule(self):
        parent = find_matching_rule(["DT", "NN"], self.rules)
        self.assertEqual(parent, "NP")

    def test_parse(self):
        words = tokenize_sentence("The man likes the dog")
        pos_tags = get_pos_tags(words, self.lexicon)
        nodes = parse(words, pos_tags, self.rules)

        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].label, "S")

    def test_partial_parse(self):
        words = tokenize_sentence("The man likes the dog man")
        pos_tags = get_pos_tags(words, self.lexicon)
        nodes = parse(words, pos_tags, self.rules)

        self.assertGreater(len(nodes), 1)

    def test_check_agreement(self):
        words = tokenize_sentence("The man likes the dog")
        pos_tags = get_pos_tags(words, self.lexicon)

        self.assertTrue(
            check_agreement(words, pos_tags, self.lexicon)
        )

    def test_invalid_agreement(self):
        words = tokenize_sentence("The man like the dog")
        pos_tags = get_pos_tags(words, self.lexicon)

        self.assertFalse(
            check_agreement(words, pos_tags, self.lexicon)
        )

    def test_bracketed_structure(self):
        node = Node("NN", [Node("man")])
        self.assertEqual(node.to_brackets(), "[NN man]")

    def test_print_tree(self):
        node = Node("NN", [Node("man")])
        node.print_tree()

        self.assertEqual(node.label, "NN")
        self.assertEqual(node.children[0].label, "man")

    def test_intransitive_verb(self):
        words = tokenize_sentence("The man eats")
        pos_tags = get_pos_tags(words, self.lexicon)
        nodes = parse(words, pos_tags, self.rules)

        self.assertEqual(nodes[0].label, "S")
        self.assertTrue(check_agreement(words, pos_tags, self.lexicon))


if __name__ == "__main__":
    unittest.main()
