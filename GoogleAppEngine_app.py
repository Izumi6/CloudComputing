# ================================================================
#  Google App Engine - Simple Addition Program
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
# pip install google-cloud-sdk
# gcloud init
# gcloud auth login
# python GoogleAppEngine_app.py
# gcloud app deploy
# gcloud app browse
