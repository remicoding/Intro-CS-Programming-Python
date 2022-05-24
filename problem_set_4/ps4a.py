"""
Remi Coding
Problem Set 4 from Introduction to Computer Science and Programming in Python
MITOPENCOURSEWARE
"""

def get_permutations(sequence):
    """
    Enumerates all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string
    Returns: a list of all permutations of sequence
    """
    # if only one letter returns in a list
    if len(sequence) == 1:
        return [sequence]
    # keeps first letter and recursively go through sequence
    # inserts first letter in returned list of sequence
    return insert_letter(sequence[0], get_permutations(sequence[1:]))

def insert_letter(letter, char_lst):
    """
    Iteratively insert letter in between characters of a string

    letter: string (char)
    char_lst: list of strings
    returns: list of strings
    """
    # number of possible space to insert letter
    space_num = len(char_lst[0]) + 1
    # total number of permutation possible
    permutation_num = space_num * len(char_lst)
    # initializing indexes for characters within each strings in char_lst
    char_ind = 1
    char_lst_ind = 0
    # initializing the set of permutation with the first possible permutation
    permutation_set = set([letter + char_lst[char_lst_ind]])
    for ind in range(1, permutation_num):
        # if char_lst contains one character only
        if permutation_num == 2:
            permutation_set.add(char_lst[char_lst_ind] + letter)
        # if all possible permutations of the current string is reached
        elif ind % space_num == 0:
            char_lst_ind += 1
            char_ind = 1
            permutation_set.add(letter + char_lst[char_lst_ind])
        # insert letter at each possible space to create permuation string
        else:
            permutation_set.add(char_lst[char_lst_ind][:char_ind] + letter + char_lst[char_lst_ind][char_ind:])
            char_ind += 1
    return list(permutation_set)
    
def main():
    example_input = 'ab'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    

if __name__ == '__main__':
    main()