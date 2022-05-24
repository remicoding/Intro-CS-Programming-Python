import unittest
from ps4a import *

class TestProblemSet(unittest.TestCase):

    def test_get_permutations(self):
        """
        Unit test for ps4a get_permutations
        """
        permutation_dct = {"a": ["a"],
                           "ab": ["ab", "ba"],
                           "abc": ["abc", "bac", "bca", "acb", "cab", "cba"],
                           "nun": ["nun", "unn", "nnu"]}
        for string, permutation_lst in permutation_dct.items():
            self.assertCountEqual(get_permutations(string), permutation_lst)

if __name__ == "__main__":
    unittest.main()