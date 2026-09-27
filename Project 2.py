print("Welcome to my second project in Python!")
input("Press Enter to continue...")
print("This project is a simple calculator that can perform basic arithmetic operations.")
input("Press Enter to continue...")

first_number = float(input("Please enter the first number: "))
second_number = float(input("Please enter the second number: "))
operation = input("Please enter the operation you would like to perform (+, -, *, /): ")
#Reasultsssssssssssssssssssss
if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number == 0:
        print("Error: Division by zero is not allowed.")
        result = None
    else:
        result = first_number / second_number
else:
    print("Error: Invalid operation.")
    result = None

if result is not None:
    print("The result is:", result)
input("Press Enter to exit...")