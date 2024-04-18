# def get_numeric_input(prompt):
#     while True:
#         try:
#             value = float(input(prompt))
#             return value
#         except ValueError:
#             print("Error: Please enter a numerical value.")

# try:
#     num1 = get_numeric_input("Enter the first number: ")
#     num2 = get_numeric_input("Enter the second number: ")

#     result = num1 + num2
#     print("Sum of the numbers:", result)

# except TypeError as e:
#     print("TypeError occurred:", e)


def get_numeric_input(prompt):
 
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Invalid input. Please Input a valid number.")
 
n1 = get_numeric_input("Input the first number: ")
n2 = get_numeric_input("Input the second number: ")
result = n1 * n2
print("Product of the said two numbers:", result)