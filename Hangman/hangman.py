"""
This is a Hangman Game - The computer picks a word from a given set of repository of words
and the user has to guess it within a limited numnber of attempts
"""

import random as rd
import string
from words import words

def get_valid_word(words):
    """
    Choose a valid word from a given set of words
    """
    word = rd.choice(words)

    while "-" in word or " " in word:
        word = rd.choice(words)
    
    return word

def hangman():
    """
    Initiate playing of hangman
    """
    word = get_valid_word(words).upper() # Get a valid word and convert to Uppercase
    print(f"\n\nYou have to guess a word with {len(word)} letters")

    letters = set(word) # Set of unique letters in the word
    alphabet = set(string.ascii_uppercase) # List of all alphabets in Uppercase
    used = set() # Set of all unique letters already used
    attempts = 10 # No. of attempts to guess the word correctly

    while len(letters) > 0 and attempts > 0:
        
        # Create a list with all the letters which are both in used letters set and in the word and replacing the others with "-"
        # IMPORTANT
        current_word = [letter if letter in used else "-" for letter in word] 

        print("\nYou have used these letters : ", " ".join(used)) # Print used letters by joining the used letter set

        print("\nThe current word you've guessed until now :  ", " ".join(current_word)) # Print current word by joining the prev list

        print(f"\n\n********* Lives left : {attempts} ***********")
        
        user_input = input("\nGuess a letter in the word : ").upper() # Takes a user input for a letter to guess

        # Check if the user input letter is still unused or not
        if user_input in alphabet - used:
            used.add(user_input)
            
            # Check if user input is included in the word
            if user_input in letters:
                print("\nYour guess is correct!")
                letters.remove(user_input)

            else:
                print("\nWrong input! Try a different letter!")
                attempts -= 1
                
        else:
            print("\nYou have already typed the character. Try with different character!")
        
    # Check if number of lives left is greater than 0
    if attempts > 0:
        print(f"\n\nCongratulaions! You have guessed the word! The word is {word}\n\n")
    else:
        print(f"\n\nSorry you have exhausted all your lives. The word is {word}\n\n")

hangman()


