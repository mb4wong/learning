# Word Counter: Develop a program that reads a text file and counts the number of words, characters, and lines in it.

import os

def welcome_message():
    print("Welcome to the Word Counter App!")

def get_valid_file_path():
    while True:
        user_input = input("Please enter the path/name to the file you want to analyze or use 'cd [directory]' to change directory or 'ls' to list files: ")

        if user_input == 'ls':
            print(f"Files in {os.getcwd()}:")
            for file in os.listdir(os.getcwd()):
                print(file)
            continue

        if user_input.startswith('cd '):
            new_dir = user_input[3: ]
            try:
                os.chdir(new_dir)
            except FileNotFoundError:
                print(f"Directory '{new_dir}' not found.")
            continue
        
        if not os.path.isfile(user_input):
            print("File not found. Please enter a valid file path.")
        elif not (user_input.endswith(".txt") or user_input.endswith(".md")):
            print("Unsupported file format. Please choose a .txt or .md file.")
        else:
            return user_input
        
def count_words_characters_lines(user_input):
    with open(user_input, 'r', encoding='utf-8') as file:
        content = file.read()
        word_count = len(content.split())
        character_count = len(content)
        line_count = len(content.splitlines())

        return word_count, character_count, line_count
    
if __name__ == "__main__":
    welcome_message()
    user_input = get_valid_file_path()

    word_count, character_count, line_count = count_words_characters_lines(user_input)

    print(f"File: {user_input}")
    print(f"Word Count: {word_count}")
    print(f"Character Count: {character_count}")
    print(f"Line Count: {line_count}")