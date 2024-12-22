def calculate(number1, number2, operation):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        if number2 != 0:
            return number1 / number2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Unsupported operation"

n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
s=input("Enter the mathematical symbol:")
result = calculate(n1, n2, s)
print(f"The result:{result}")
