import sys

def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: calculator.py <num1> <num2> <operation>")
        sys.exit(1)
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    operation = sys.argv[3]

    result = calculate(num1, num2, operation)
    print(f"Result: {result}")