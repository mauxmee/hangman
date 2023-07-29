"""
This is the first application for Alicia:
write a calculator: get two inputs from user, ask which method: (add/sub/mul/div) 
then calculate them, and print the result.
"""

"""
Issue 1: need to check input before use
issue 2: for division: the denominator should not be zero.
"""

INVALID_NUMBER = "your input isn't a number."

print("Welcome to Alicia's calculator!")
print("Please input two numbers:")


def getUserInput(prompts):
    while True:
        try:
            value = float(input(prompts))
            return value
        except ValueError:
            print(INVALID_NUMBER)


number1 = getUserInput("First number: ")
number2 = getUserInput("Second number:")

method = input("Enter the method: (add/sub/mul/div): ").lower()
if method == "add":
    number3 = number1 + number2
elif method == "sub":
    number3 = number1 - number2
elif method == "mul":
    number3 = number1 * number2
elif method == "div":
    if number2 != 0:
        number3 = number1 / number2
    else:
        print("number can't be divided by zero")
        exit(1)
else:
    print("Incorrect method")
    exit(1)

print("The result is:", number3)
