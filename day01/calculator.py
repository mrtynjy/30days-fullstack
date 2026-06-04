print("=== Simple Calculator ===")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Error: Please enter valid numbers.")
    exit()

print("Select the operation: ")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = input("Enter operation (1/2/3/4): ")

op = None
result = None
if operation == '1':
    result = num1 + num2
    op = '+'
elif operation == '2':
    result = num1 - num2
    op = '-'
elif operation == '3':
    result = num1 * num2
    op = '*'
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        op = '/'
    else:
        print("Error: Division by zero is not allowed.")
        exit()
else:
    print("Invalid operation selected.")
    exit()

print(f"{num1} {op} {num2} = {result}")
