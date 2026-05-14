# ================================================================
#  Google App Engine - Simple Calculator (calculator.py)
#  Practical: Install and Configure Google App Engine
# ================================================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"

print("===== Simple Calculator =====")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\nAddition:       {num1} + {num2} = {add(num1, num2)}")
print(f"Subtraction:    {num1} - {num2} = {subtract(num1, num2)}")
print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
print(f"Division:       {num1} / {num2} = {divide(num1, num2)}")


# ================================================================
#  Terminal Commands
# ================================================================
# git clone https://github.com/Izumi6/Cloudcomputing.git
# cd Cloudcomputing
# python3 calculator.py
