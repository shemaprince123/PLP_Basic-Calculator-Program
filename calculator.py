# Collect the first number from the user
num1 = float(input("Enter the first number: "))

# Collect the second number from the user
num2 = float(input("Enter the second number: "))

# Collect the operation from the user
operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation based on the chosen operation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    # Handle division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operation. Please use one of +, -, *, or /.")
