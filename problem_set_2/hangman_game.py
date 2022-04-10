"""
Remi Coding
Problem Set 2 from Introduction to Computer Science and Programming in Python
MITOPENCOURSEWARE
"""

import random
import string

def load_words(file_path):
    """
    Returns a list of valid words. Words are strings of lowercase letters

    file_path (string): the name of the word list file
    """
    print("Loading word list from file...")
    with open(file_path, 'r') as file_opened:
        line = file_opened.readline()
        wordlist = line.split()
        print("  ", len(wordlist), "words loaded.")
        return wordlist

def choose_word(wordlist):
    """
    Returns a word from wordlist at random

    wordlist (list): list of words (strings)
    """
    return random.choice(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    """
    Returns (boolean): if all the letters of secret_word are in letters_guessed

    -- Assumption: lowercase letters in string values

    secret_word (string): word to guess
    letters_guessed (list of letters): letters guessed
    """

    for letter in letters_guessed:
        if letter in secret_word:
            secret_word = secret_word.replace(letter, '')
            if not secret_word:
                return True
    return False

def get_guessed_word(secret_word, letters_guessed):
    """
    Returns (string): return secret_wor with underscore with space (_ ) for letters not yet guessed

    -- Assumption: lowercase letters in string values

    secret_word (string): word to guess
    letters_guessed (list of letters): letters guessed
    """

    return_string = '_' * len(secret_word)
    for letter_guessed in letters_guessed:
        for index, secret_word_letter in enumerate(secret_word):
            if letter_guessed == secret_word_letter and index == 0:
                return_string = letter_guessed + return_string[1:]
            elif letter_guessed == secret_word_letter:
                pre = return_string[:index]
                post = return_string[index + 1:]
                return_string = pre + letter_guessed + post

    return_string = return_string.replace('_', '_ ')

    return return_string

def get_available_letters(letters_guessed):
    """
    Returns (string): letters of the alphabet that have not been guessed

    -- Assumption: lowercase letters in string values

    letters_guessed (list of letters): letters guessed
    """

    all_str = string.ascii_lowercase
    for let in letters_guessed:
        all_str = all_str.replace(let, '')
    return all_str

def hangman(secret_word, wordlist):
    """
    Interactively plays the game of Hangman with the player

    secret_word (string): word to guess
    wordlist (list of string): all the words available in the game
    """
    progress_word = '_ ' * len(secret_word)
    guess_number = 6
    warning_number = 3
    letters_guessed_list = []

    start_game_stage(secret_word, warning_number)

    while ('_' in progress_word) and (guess_number > 0):
        start_round_stage(guess_number, letters_guessed_list)
        guess_number, warning_number, letters_guessed_list, progress_word, letter_guessed = player_guess(secret_word, guess_number, 
                                                                                                         warning_number, letters_guessed_list, 
                                                                                                         progress_word, wordlist)
        if letter_guessed != '*':
            end_round_stage(progress_word)
    
    end_game_stage(secret_word, guess_number)

def start_game_stage(secret_word, warning_number):
    """
    Displays the game's introduction message

    secret_word (string): word to guess
    warning_number (int): number of warnings that the player has
    """
    print('\nWelcome to the game Hangman!')
    print('--')
    print("You can choose to play the game with or without\nhint by using the '*' wild card at any moment for hints.")
    print('--')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(f'You have {warning_number} warnings left.')
    print('-' * 15)

def end_game_stage(secret_word, guess_number):
    """
    Displays the game's ending message

    secret_word (string): word to guess
    guess_number (int): number of guesses that the player has
    """
    if guess_number <= 0:
        print(f'Sorry, you ran out of guess. The word was {secret_word}.')
    else:
        print('Congratulation, you won!')
        print(f'Your total score for this game is: {get_score(guess_number, secret_word)}')

def get_score(secret_word, guess_number):
    """
    Calculates the player's score

    secret_word (string): word to guess
    guess_number (int): number of guesses that the player has
    """
    return guess_number * len(set(secret_word))

def start_round_stage(guess_number, letters_guessed_list):
    """
    Displays information player information for each game round

    guess_number (int): number of guesses that the player has
    starting_letters (string): letters available to player for the round
    """
    print(f'You have {guess_number} guesses left.')
    print(f'Available letters: {get_available_letters(letters_guessed_list)}', end='')

def end_round_stage(progress_word):
    """
    Displays the proogression at the end of the round

    progress_word (string): letters guessed at their index in the secret word
    """
    print(progress_word.replace('_', '_ '))
    print('-' * 15)

def player_guess(secret_word, guess_number, warning_number, 
                 letters_guessed_list, progress_word, wordlist):
    """
    Returns modified values of most of the entered values according to the game's rules

    secret_word (string): word to guess
    guess_number (int): number of guesses that the player has
    warning_number (int): number of warnings that the player has
    letters_guessed_list (list of char): all the letter that the player has guessed
    progress_word (string): letters guessed at their index in the secret word
    wordlist (list of string): all the words available in the game
    """
    letter_guessed = input('\nPlease guess a letter: ').lower()

    if letter_guessed == "*":
        show_possible_matches(progress_word, wordlist)
    elif letter_guessed not in get_available_letters(letters_guessed_list):
        guess_number, warning_number = reduce_warning_number(letter_guessed, 
                                                             warning_number, 
                                                             guess_number)
    elif letter_guessed in secret_word:
        letters_guessed_list, progress_word = correct_guess(secret_word,
                                                            letters_guessed_list, 
                                                            letter_guessed, 
                                                            progress_word)
    else:
        guess_number, letters_guessed_list = reduce_guess_number(guess_number, 
                                                                 letters_guessed_list, 
                                                                 letter_guessed)
    
    return guess_number, warning_number, letters_guessed_list, progress_word, letter_guessed

def reduce_warning_number(letter_guessed, warning_number, guess_number):
    """
    Reduces the number of warnings (and guesses) according to the game's rules

    letter_guessed (char): letter guessed by the player
    warning_number (int): number of warnings that the player has
    guess_number (int): number of guesses that the player has
    """
    warning_number -= 1

    if letter_guessed in string.ascii_lowercase:
        print(
            "Oops! You've already guessed that letter. You now have ",
            end='')
    else:
        print('Oops! That is not a valid letter. You have ', end='')

    if warning_number < 0:
        guess_number -= 1
        print('no warning left so you lose one guess: ', end='')
    elif warning_number == 1:
        print(f'{warning_number} warning left: ', end='')
    else:
        print(f'{warning_number} warnings left: ', end='')
    
    return guess_number, warning_number

def correct_guess(secret_word, letters_guessed_list, letter_guessed, progress_word):
    """
    Modifies the entered values according to the game's rule if the guess is correct

    secret_word (string): word to guess
    letters_guessed_list (list of char): all the letter that the player has guessed
    letter_guessed (char): letter guessed by the player
    progress_word (string): letters guessed at their index in the secret word
    """
    letters_guessed_list.append(letter_guessed)
    progress_word = progress_word.replace(' ', '')
    word_string = get_guessed_word(secret_word, letter_guessed)
    word_string = word_string.replace(' ', '')

    for index, letter in enumerate(word_string):
        if letter != progress_word[index] and progress_word[index] == '_':
            progress_word = progress_word[:index] + word_string[
                index] + progress_word[index + 1:]
    print('Good guess: ', end='')

    return letters_guessed_list, progress_word

def reduce_guess_number(guess_number, letters_guessed_list, letter_guessed):
    """
    Reduces the number of guesses according to the game's rules

    guess_number (int): number of guesses that the player has
    letters_guessed_list (list of char): all the letter that the player has guessed
    letter_guessed (char): letter guessed by the player
    """
    letters_guessed_list.append(letter_guessed)

    if letter_guessed in 'aeiou':
        guess_number -= 2
    else:
        guess_number -= 1

    print('Oops! That letter is not in my word: ', end='')

    return guess_number, letters_guessed_list

def match_with_gaps(progress_word, other_word):
    """
    Returns if the guessed letters of progress_word match the correspoding 
    letters of other_word

    progress_word (string): letters guessed at their index in the secret word
    other_word (string): word from the world list available to in the game
    """
    progress_word = progress_word.replace(" ", "")
    if len(progress_word) != len(other_word):
        return False
    else:
        for index, letter in enumerate(progress_word):
            if letter != "_" and progress_word[index] != other_word[index]:
                return False
        return True

def show_possible_matches(progress_word, wordlist):
    """
    Displays all words in wordlist that match progress_word

    progress_word (string): letters guessed at their index in the secret word
    wordlist (list of string): all the words available in the game
    """
    for word in wordlist:
        if match_with_gaps(progress_word, word):
            print(word, end=" ")
    print('\n' + '-' * 15)

def main():
    """
    Runs the program for the Hungman game
    """
    wordlist_filename = "words.txt"
    wordlist = load_words(wordlist_filename)
    secret_word = choose_word(wordlist)
    hangman(secret_word, wordlist)


if __name__ == '__main__':
    main()