"""
Remi Coding
Problem Set 3 from Introduction to Computer Science and Programming in Python
MITOPENCOURSEWARE
"""

import random
import math
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
}

WORDLIST_FILENAME = "ps3/words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    # open_file: file
    with open(WORDLIST_FILENAME, 'r') as open_file:
        # wordlist: list of strings
        wordlist = []
        for line in open_file:
            wordlist.append(line.strip().lower())
        print("  ", len(wordlist), "words loaded.")
        return wordlist

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower()
    word_length = len(word)
    
    first_comp = sum([SCRABBLE_LETTER_VALUES[letter] for letter in word])
    second_comp = max(7 * word_length - 3 * (n - word_length), 1)
    
    return first_comp * second_comp

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freq: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))
    hand['*'] = 1

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    word_dct = get_frequency_dict(word.lower())
    new_hand = {}
    
    for letter in hand.keys():
        if letter in word_dct.keys():
            freq = hand[letter] - word_dct[letter]
            if freq > 0:
                new_hand[letter] = freq
        else:
            new_hand[letter] = hand[letter]
        
    return new_hand

def is_valid_word(word, hand, word_lst):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    
    if '*' in word:
        word, hand = use_wildard(word, hand, word_lst)

    word_dct = get_frequency_dict(word)

    return check_word(word, hand, word_lst, word_dct)

def check_word(word, hand, word_lst, word_dct):
    """
    Verifies if a word given by a player obeys the rules of the game.
    The word needs to be in the word list it is composed entirely of 
    letters from the current hand.

    word: string
    hand: dictionary (string -> int)
    word_lst: list of lowercase strings
    word_dct: dictionary (string -> int)
    returns: boolean
    """
    if word not in word_lst:
        return False
    for letter in word:
        if letter not in hand.keys() or word_dct[letter] > hand.get(letter, 0):
            return False
    return True

def use_wildard(word, hand, word_lst):
    """
    Checks to see what possible words can be formed by replacing the wildcard
    with other vowels.

    word: string
    hand: dictionary (string -> int)
    word_lst: list of lowercase strings
    returns: string, dictionary (string -> int)
    """
    for vowel in VOWELS:
        new_word = word.replace('*', vowel)
        new_hand = hand.copy()
        new_hand[vowel] = new_hand.pop('*')
        if new_word in word_lst:
            return new_word, new_hand

    return word, hand

def play_hand(hand, word_lst):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_lst: list of lowercase strings
      returns: the total score for the hand
    """
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    hand_len = calculate_handlen(hand)
    while hand_len > 0:
        # Display the hand
        print("\nCurrent Hand:", end=' ')
        display_hand(hand)
        # Ask user for input
        word = input('Enter word, or "!!" to indicate that you are finished: ')
        # If the input is two exclamation points:
        if word == "!!":
            # End the game (break out of the loop)
            print("Total score for this hand: " + str(total_score) + " points")
            break
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(word, hand, word_lst):
                # Tell the user how many points the word earned,
                score = get_word_score(word, hand_len)
                print('"' + word + '" earned ' + str(score) + " points.", end=' ')
                # and the updated total score
                total_score += score
                print("Total: " + str(total_score) + " points")
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print("That is not a valid word. Please choose another word.")
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, word)
            hand_len = calculate_handlen(hand)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    if word != "!!":
        print("\nRan out of letters. Total score: " + str(total_score) + " points")
    
    # Return the total score as result of function
    return total_score

def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: int
    """
    return sum([value for key, value in hand.items()])

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    letter = letter.lower()
    # get all letters in the hand
    keys_lst = list(hand.keys())
    # if the user provides a letter not in the hand
    if letter not in keys_lst or letter == '*':
        return hand
    # initializing the alphabet
    available_let = string.ascii_lowercase
    # removing all the letters already in the hand
    for char in keys_lst:
        available_let = available_let.replace(char, '')
    # selecting a random letter from the rest of the letters
    random_let = random.choice(available_let)
    # do not mutate hand
    hand_copy = hand.copy()
    # replacing the user's letter with a random letter
    hand_copy[random_let] = hand_copy.pop(letter)

    return hand_copy

def play_game(word_lst):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    # user input a total number of hands
    hands_num = int(input("Enter total number of hands: "))
    # accumulate the score for each hand
    total_hand_score = 0
    hand_score_1 = 0
    hand_score_2 = 0
    subs = True
    replays = True
    for _ in range(hands_num):
        # deal hand
        hand = deal_hand(HAND_SIZE)
        # print current hand
        print("Current hand:", end=' ')
        display_hand(hand)
        # only one substitution is allowed per game
        if subs:
            sub_let = str.lower(input("Would you like to substitute a letter? "))
            # substitute letter and make sure the user is not asked again
            if sub_let == "yes":
                letter = str.lower(input("Which letter would you like to replace: "))
                hand = substitute_hand(hand, letter)
                subs = False
        # play with hand
        hand_score_1 = play_hand(hand, word_lst)
        print("--------------")
        # only one hand replay is allowed per game
        if replays:
            replay_hand = str.lower(input("Would you like to replay the hand? "))
            # replay hand and make sure the user is not asked again
            if replay_hand == "yes":
                hand_score_2 = play_hand(hand, word_lst)
                replays = False
                print("--------------")
        # adds the max of either hand play or hand replay to the total
        total_hand_score += max(hand_score_1, hand_score_2)
    # display total score for the game
    print("Total score over all hands:", total_hand_score)

def main():
    word_lst = load_words()
    play_game(word_lst)

if __name__ == "__main__":
    main()