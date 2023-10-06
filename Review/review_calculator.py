# TASK: Create a simple command-line calculator that can perform basic arithmetic operations like addition, subtraction, multiplication, and division.
# Version 2: User enters number 1 and number 2 separated by a comma; then selects what arithmetic operation to complete.

def minus(numbers):
    return numbers[0] - sum(numbers[1:])

def multiply(numbers):
    result = 1
    for i in numbers:
        result = result*i
    return result

def division(numbers):
    result = numbers[0]
    for i in range(len(numbers)-1):
        result = result/numbers[i+1]
    return result

def calculator():
    
    while True:
        try:
            user_input_number = input("Enter all the numbers you wish to compute with, separated by a space: ")

            numbers = user_input_number.split()
            
            if len(numbers) < 2:
                print("Invalid input - less than 2 numbers input. Please enter two numbers separated by a comma")
                continue
            
            for i in range(len(numbers)):
                numbers[i] = float(numbers[i])
            
        except ValueError:
            print("Invalid input - text detected. Please try again.")
            continue

        break

    while True:
        user_input_function = input("[1] Addition\n[2] Subtraction\n[3] Multiplication\n[4] Division\nEnter the corresponding number for the function you want to perform: ")

        if user_input_function not in ['1','2','3','4']:
            print("Invalid input.")
            continue

        break

    if user_input_function == '1':
        result = sum(numbers)
    elif user_input_function == '2':
        result = minus(numbers)
    elif user_input_function == '3':
        result = multiply(numbers)
    elif user_input_function == '4':
        result = division(numbers)

    print(result)

if __name__ == "__main__":
    calculator()