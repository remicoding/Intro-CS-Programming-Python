import unittest
from ps4a import *
from ps4b import *

class TestProblemSet(unittest.TestCase):

    def test_ps4a_get_permutations(self):
        """
        Unit test for ps4a get_permutations
        """
        permutation_dct = {"a": ["a"],
                           "ab": ["ab", "ba"],
                           "abc": ["abc", "bac", "bca", "acb", "cab", "cba"],
                           "nun": ["nun", "unn", "nnu"]}
        for string, permutation_lst in permutation_dct.items():
            self.assertCountEqual(get_permutations(string), permutation_lst)

    def test_ps4b_plaintext_message(self):
        """
        Unit test for ps4b PlaintextMessage class
        """
        message_dct = {"hello": "jgnnq", "I'm fine": "K'o hkpg", "Hello, World!": "Jgnnq, Yqtnf!", '': ''}
        for message, encrypted in message_dct.items():
            self.assertEqual(PlaintextMessage(message, 2).get_message_text_encrypted(), encrypted)
    
    def test_ps4b_ciphertext_message(self):
        """
        Unit test for ps4b CiphertextMessage class
        """
        message_dct = {"hello": "jgnnq", "I'm fine": "K'o hkpg", "Hello, World!": "Jgnnq, Yqtnf!"}
        for message, encrypted in message_dct.items():
            self.assertEqual(CiphertextMessage(encrypted).decrypt_message(), (24, message))


if __name__ == "__main__":
    unittest.main(verbosity=2)