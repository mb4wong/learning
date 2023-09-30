# TASK: Guess the Number Game: Create a number guessing game where the computer generates a random number, and the user has to guess it within a certain number of attempts.
# I want three difficulties: (1) Easy: Guess between 1-10; (2) Medium: Guess between 1-100; (3) Hard: Guess between 1-1000.
# All inputs must be integers.
# I want to display the users win rate by each level

import os
import random

def play_level(difficulty, range_max):
    level_attempts = 0
    level_wins = 0

    os.system('clear')
    if level_attempts == 0:
        print(f"Welcome to the {difficulty.upper()} level")
        print("This is your first attempt! Let's go!")
    else:
        print(f"Welcome to the {difficulty.upper()} level")
        print(f"You've currently gotten {level_wins} correct out of {level_attempts} in the {difficulty.upper()} level.")
    
    while True:
        target_number = random.randint(0, range_max)

        user_guess = input(f"Please enter your guess. The range is between 0 and {range_max}: ").lower()
        level_attempts += 1

        if user_guess == "end":
            print("Taking you back to the menu...")
            os.system('clear')
            return level_attempts, level_wins
        
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please enter a valid number or 'END' to return to the menu.")
            continue

        if user_guess < 0 or user_guess > range_max:
            print("Number out of range. You lose.")
        elif user_guess == target_number:
            print(f"Congrats! {user_guess} was the right number!")
            level_wins += 1
        else:
            print(f"Sorry, {user_guess} was not the right number. It was actually {target_number}")

def main():
    print("Welcome to the number guesser game!")

    while True:
        difficulty = input("Please choose which level you want (easy/medium/hard): ")
        if difficulty == "easy":
            range_max = 10
        elif difficulty == "medium":
            range_max = 100
        elif difficulty == "hard":
            range_max = 1000
        else:
            print("Invalid difficulty level. Please choose from easy, medium, or hard.")
            continue
        
        attempts, wins = play_level(difficulty, range_max)
        print(f"You played {attempts} times and won {wins} times in the {difficulty.upper()} level.")

if __name__ == "__main__":
    main()