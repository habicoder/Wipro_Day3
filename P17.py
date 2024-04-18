''''
Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

'''
def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Invalid input. Please Input a valid number.")


n1 = get_numeric_input("first number: ")
n2 = get_numeric_input("second number: ")
result = n1 * n2
print("product of the numbers:", result)