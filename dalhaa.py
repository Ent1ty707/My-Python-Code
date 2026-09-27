from datetime import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")
answer = input("Do you want to know your year of birth? (yes/no): ").lower()
if answer == "yes":
    current_year = datetime.now().year
    birth_year = current_year - age
    print(f"Hello {name}, you are {age} years old, your hobby is {hobby}, and you were born in {birth_year}. Thank you mr cimmino for looking at my 1st project.")
else:
    print(f"Hello {name}, you are {age} years old and your hobby is {hobby}. Thank you mr cimmino for looking at my 1st project.")
