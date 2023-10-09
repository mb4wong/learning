# Hangman Game: Implement a text-based version of the classic Hangman game where players guess letters to reveal a hidden word.

import requests
from bs4 import BeautifulSoup
import random
import os

words = []
random_word = ""

def get_word_list():
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(url)
    print("Initializing...")

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        words.extend(soup.text.split())
        for word in reversed(words):
            if len(word) < 3:
                words.remove(word)
        os.system('clear')
        print("Game initialized!")
        return words
    else:
        os.system('clear')
        print(f"Failed to get list of words. Status code: {response.status_code}")

def get_random_word(words):
    random_word = random.choice(words)
    unique_letters = set(random_word.lower())
    return random_word, unique_letters

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "[?]"
    return displayed_word

def hangman():
    print("Welcome to the hangman game!")
    get_word_list()
    random_word, unique_letters = get_random_word(words)
    guessed_letters = set()
    lives = 10

    while lives > 0 and len(unique_letters) > 0:
        displayed = display_word(random_word, guessed_letters)
        print(displayed)
        print(f"Lives: {'❤' * lives}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.\n")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in random_word:
            print(f"Good guess! '{guess}' is in the word.\n")
            unique_letters.remove(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.\n")
            lives -= 1
    
    if lives <= 0:
        print("Out of lives! You lost.")
        print(f"The word was {random_word}")
    
    if len(unique_letters) == 0:
        print(f"Congrats! You've guessed the right word which was {random_word}")

if __name__ == "__main__":
    hangman()