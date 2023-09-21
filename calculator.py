# TASK: Create a simple command-line calculator that can perform basic arithmetic operations like addition, subtraction, multiplication, and division.
# Version 1: User enters number 1; then enters number 2; then selects what arithmetic operation to complete.
# Version 2: User enters number 1 and number 2 separated by a comma; then selects what arithmetic operation to complete.
# Version 3: User can enter entire command "[X] times [Y]" Able to break string up into various components and then execute specific instructions.

##### VERSION 1

print("Please enter your first integer: ")
num_1 = int(input())
print("Your first number is", num_1,". Please input your second integer: ")
num_2 = int(input())
print("Your two numbers are:", num_1, "and", num_2,". What arithmetic operation would you like to perform with these two?")
print("Type 1 for addition\nType 2 for subtraction\nType 3 for multiplication\nType 4 for division")
operation = int(input())
if operation == 1:
    print(num_1, "+", num_2, "=", num_1 + num_2)
elif operation == 2:
    print(num_1, "-", num_2, "=", num_1 - num_2)
elif operation == 3:
    print(num_1, "*", num_2, "=", num_1 * num_2)
elif operation == 4:
    print(num_1, "/", num_2, "=", num_1 / num_2)
else:
    print("Boy you dumb you didn't follow the instructions")

