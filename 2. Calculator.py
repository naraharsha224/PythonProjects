# Project: Calculator

# This is a simple calculator that can perform basic arithmetic operations

# Step 1: Get the input from the user

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operator = input("Enter the operator: ")

# Step 2 : Perform the arithmetic operations
# Convert the input numbers to float
num1 = float(num1)
num2 = float(num2)

# # Use a conditional statement to check the operator and perform the corresponding operation

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print("invalid operator")

# Step 3 : Display the result to the user
print("Result: ",result)
