# Word Generator

import random
import string

def generate_random_word():
    length = random.randint(3,15)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def create_word_list_file(file_name, num_words):
    with open(file_name, 'w') as word_file:
        for _ in range(num_words):
            random_word = generate_random_word()
            delimiter =  ' ' if random.choice([0,1]) == 1 else "\n"
            word_file.write(random_word + delimiter)

num_words = int(input("Enter the number of words you want in the list: "))
file_name = f"{num_words}_word_list.txt"
create_word_list_file(file_name, num_words)
print(f"{num_words} random words have been saved to '{file_name}'.")
