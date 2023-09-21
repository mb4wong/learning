# TASK: Create a simple command-line calculator that can perform basic arithmetic operations like addition, subtraction, multiplication, and division.
# Version 1: User enters number 1; then enters number 2; then selects what arithmetic operation to complete.
# Version 2: User enters number 1 and number 2 separated by a comma; then selects what arithmetic operation to complete.
# Version 3: User can enter entire command "[X] times [Y]" Able to break string up into various components and then execute specific instructions.

##### VERSION 1

def calculator():
    print("This is my first calculator")

    try:
        num_1 = float(input("Enter your first number: "))
        num_2 = float(input("Enter your second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numers.")
        return
    
    print("Choose an operation:")
    print("1 for addition")
    print("2 for subtraction")
    print("3 for multiplication")
    print("4 for division")

    operation = input("Enter the operation number: ")

    if operation not in ['1', '2', '3', '4']:
        print("Invalid operation. Please choose a valid operation.")
        return
    
    if operation == '1':
        result = num_1 + num_2
        operator = '+'
    elif operation == '2':
        result = num_1 - num_2
        operator = '-'
    elif operation == '3':
        result = num_1 * num_2
        operator = '*'
    else:
        if num_2 == 0:
            print("Error: Division byu zero.")
            return
        result = num-1 / num_2
        operator = '/'

    print(f"{num_1} {operator} {num_2} = {result}")