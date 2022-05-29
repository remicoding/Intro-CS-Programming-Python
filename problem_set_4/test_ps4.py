import unittest
from ps4a import *
from ps4b import *
from ps4c import *

class TestProblemSet(unittest.TestCase):

    def test_ps4a_get_permutations(self):
        """
        Unit test for ps4a get_permutations function
        """
        permutation_dct = {"a": ["a"],
                           "ab": ["ab", "ba"],
                           "abc": ["abc", "bac", "bca", "acb", "cab", "cba"],
                           "nun": ["nun", "unn", "nnu"]}
        for string, permutation_lst in permutation_dct.items():
            self.assertCountEqual(get_permutations(string), permutation_lst)

    def test_ps4b_get_message_text_encrypted(self):
        """
        Unit test for ps4b PlaintextMessage class, get_message_text_encrypted method
        """
        message_dct = {"hello": "jgnnq", "I'm fine": "K'o hkpg", "Hello, World!": "Jgnnq, Yqtnf!", '': ''}
        for message, encrypted in message_dct.items():
            self.assertEqual(PlaintextMessage(message, 2).get_message_text_encrypted(), encrypted)
    
    def test_ps4b_decrypt_message(self):
        """
        Unit test for ps4b CiphertextMessage class, decrypt_message method
        """
        message_dct = {"hello": "jgnnq", "I'm fine": "K'o hkpg", "Hello, World!": "Jgnnq, Yqtnf!"}
        for message, encrypted in message_dct.items():
            self.assertEqual(CiphertextMessage(encrypted).decrypt_message(), (24, message))

    def test_ps4c_build_transpose_dict(self):
        """
        Unit test for ps4c SubMessage class, build_transpose_dict method
        """
        "aeiou"
        vowels_permutations_dct = {"eaiuo": {'a': 'e', 'e': 'a', 'i': 'i', 'o': 'u', 'u': 'o', 'A': 'E', 'E': 'A', 'I': 'I', 'O': 'U', 'U': 'O'}, 
                                   "uaeio": {'a': 'u', 'e': 'a', 'i': 'e', 'o': 'i', 'u': 'o', 'A': 'U', 'E': 'A', 'I': 'E', 'O': 'I', 'U': 'O'}}
        for vowels_permutation, transpose_dct in vowels_permutations_dct.items():
            self.assertDictEqual(SubMessage("").build_transpose_dict(vowels_permutation), transpose_dct)

    def test_ps4c_apply_transpose(self):
        """
        Unit test for ps4c SubMessage class, apply_transpose method
        """
        message_dct = {"eaiuo": ("Hello World!", "Hallu Wurld!"),
                       "uaeio": ("I am doing fine.", "E um dieng fena.")}
        for vowels_permutation, (message, encrypted) in message_dct.items():
            message = SubMessage(message)
            self.assertEqual(message.apply_transpose(message.build_transpose_dict(vowels_permutation)), encrypted)

    def test_ps4c_decrypt_message(self):
        """
        Unit test for ps4c EncryptedSubMessage class, decrypt_message method
        """
        message_dct = {"Hello World!": "Hallu Wurld!",
                       "I am doing fine.": "E um dieng fena."}
        for message, encrypted in message_dct.items():
            self.assertEqual(EncryptedSubMessage(encrypted).decrypt_message(), message)


if __name__ == "__main__":
    unittest.main(verbosity=2)