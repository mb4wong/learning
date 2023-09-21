# TASK: Create a simple command-line calculator that can perform basic arithmetic operations like addition, subtraction, multiplication, and division.
# Version 1: User enters number 1; then enters number 2; then selects what arithmetic operation to complete.
# Version 2: User enters number 1 and number 2 separated by a comma; then selects what arithmetic operation to complete.
# Version 3: User can enter entire command "[X] times [Y]" Able to break string up into various components and then execute specific instructions.

##### VERSION 2

def calculator():
    print("This is my first calculator, but version 2.0")

    while True:
        try:
            num_prompt = input("Enter your numbers, separated by a comma (e.g. 7.1,3.6): ")
            num_input = num_prompt.split(',')

            if len(num_input) != 2:
                print("Invalid input. Please enter two numbers separated by a comma")
                continue
        
            num_1 = float(num_input[0])
            num_2 = float(num_input[1])
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        break
    
    print("Choose an operation:")
    print("1 for addition")
    print("2 for subtraction")
    print("3 for multiplication")
    print("4 for division")

    while True:
        operation = input("Enter the operation number: ")

        if operation not in ['1', '2', '3', '4']:
            print("Invalid operation. Please choose a valid operation.")
            continue

        break 
    
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
        result = num_1 / num_2
        operator = '/'

    print(f"{num_1} {operator} {num_2} = {result}")

if __name__ == "__main__":
    calculator()