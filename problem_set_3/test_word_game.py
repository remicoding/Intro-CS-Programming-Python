"""
Remi Coding
Problem Set 3 Test from Introduction to Computer Science and Programming in Python
MITOPENCOURSEWARE
"""
import unittest
from word_game import *

class TestWordGame(unittest.TestCase):

    def test_get_word_score(self):
        """
        Unit test for get_word_score
        """
        # dictionary of words and scores
        words = {("", 7): 0, ("it", 7): 2, ("was", 7):54, ("weed", 6): 176,
                ("scored", 7): 351, ("WaYbILl", 7): 735, ("Outgnaw", 7): 539,
                ("fork", 7): 209, ("FORK", 4): 308}
        for (word, n) in words.keys():
            self.assertEqual(get_word_score(word, n), words[(word, n)])

    def test_update_hand(self):
        """
        Unit test for update_hand
        """
        # test 1
        hand_orig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
        hand_copy = hand_orig.copy()
        word = "quail"
        self.assertEqual(update_hand(hand_copy, word), {'l':1, 'm':1})
        self.assertEqual(hand_orig, hand_copy)
        
        # test 2
        hand_orig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
        hand_copy = hand_orig.copy()
        word = "Evil"
        self.assertEqual(update_hand(hand_copy, word), {'v':1, 'n':1, 'l':1})
        self.assertEqual(hand_orig, hand_copy)

        # test 3
        hand_orig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        hand_copy = hand_orig.copy()
        word = "HELLO"
        self.assertEqual(update_hand(hand_copy, word), {})
        self.assertEqual(hand_orig, hand_copy)

    def test_is_valid_word(self):
        """
        Unit test for is_valid_word
        """
        word_lst = load_words()

        # test 1
        word = "hello"
        hand_orig = get_frequency_dict(word)
        hand_copy = hand_orig.copy()
        self.assertEqual(is_valid_word(word, hand_copy, word_lst), True)
        self.assertEqual(hand_orig, hand_copy)

        # test 2
        hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
        word = "Rapture"
        self.assertEqual(is_valid_word(word, hand, word_lst), False)

        # test 3
        hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
        word = "honey"
        self.assertEqual(is_valid_word(word, hand, word_lst), True)

        # test 4
        hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
        word = "honey"
        self.assertEqual(is_valid_word(word, hand, word_lst), False)

        # test 5
        hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
        word = "EVIL"
        self.assertEqual(is_valid_word(word, hand, word_lst), True)

        # test 6
        word = "Even"
        self.assertEqual(is_valid_word(word, hand, word_lst), False)

    def test_wildcard(self):
        """
        Unit test for is_valid_word with wildcard
        """
        word_lst = load_words()

        # test 1
        hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
        word = "e*m"
        self.assertEqual(is_valid_word(word, hand, word_lst), False)

        # test 2
        hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
        word = "honey"
        self.assertEqual(is_valid_word(word, hand, word_lst), False)

        # test 3
        hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
        word = "h*ney"
        self.assertEqual(is_valid_word(word, hand, word_lst), True)

        # test 4
        hand = {'c': 1, 'o': 1, '*': 1, 'w': 1, 's':1, 'z':1, 'y': 2}
        word = "c*wz"
        self.assertEqual(is_valid_word(word, hand, word_lst), False)

        # dictionary of words and scores WITH wildcards
        words = {("h*ney", 7):290, ("c*ws", 6):176, ("wa*ls", 7):203}
        for (word, n) in words.keys():
            self.assertEqual(get_word_score(word, n), words[(word, n)])

if __name__ == "__main__":
    unittest.main()