# TASK: Guess the Number Game: Create a number guessing game where the computer generates a random number, and the user has to guess it within a certain number of attempts.
# I want three difficulties: (1) Easy: Guess between 1-10; (2) Medium: Guess between 1-100; (3) Hard: Guess between 1-1000.
# All inputs must be integers.
# I want to display the users win rate by each level

import random

def number_game(difficulty, range_max):
    level_attempts = 0
    level_wins = 0

    while True:
        correct_number = random.randint(1, range_max)
        level_attempts += 1

        user_guess = input(f"Welcome to the {difficulty} level. Enter your guess or type end to quit: ")

        if user_guess.lower() == "end":
            print("Taking you to the menu.")
            break
        
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if user_guess == str(correct_number):
            level_wins += 1
            print(f"Congrats! {user_guess} was the right number!")
        else:
            print(f"Your guess of '{user_guess}' is wrong.")
    
    print(f"Final score: {level_wins} wins on {level_attempts} attempts!")
    
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
    
        number_game(difficulty, range_max)

if __name__ == "__main__":
    main()