def calculator():
    print("Simple Python calc")
    print("Operators:- +, -, *, /")

    num1 = float(input("first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("second number: "))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero! "
        result = num1 / num2
    else:
        return "Invalid operator!"

    return f"Result: {result}"

print(calculator())