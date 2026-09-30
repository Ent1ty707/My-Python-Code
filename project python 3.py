name = input("Enter your name:")
age = int(input("Enter your age:"))
email = input("Enter your email address:")
Number = input("Enter your phone number:")
#store this stuff
print("Hello "+name+"Welcome to DT You have signed up with the following details:")
print("Name: "+name)
print("Age: "+str(age))
if age < 18:
    print("You are a minor. Please ensure you have parental consent to use this service.")
print("Email: "+email)
print("Phone Number: "+Number)
confirmation = input("Can we send you a confirmation email to "+email+"? (yes/no): ").strip().casefold()
if confirmation == "yes":
    print("Thank you! A confirmation email will be sent to "+email)
else:
    print("Thank you! You will not receive a confirmation email.")
    print("We will keep you updated on the latest news and events related to your interests.")

Interest = input("What are your interests? (e.g., sports, music, technology): ")
print("Nice! We will keep you updated on topics related to "+Interest+".")

Gcse_options = input("What are you choosing for your GCSE options? (e.g., Maths, Science, History, Music): ").strip().casefold()
if Gcse_options in ("maths", "math"):
    print("Great choice! Maths is a fundamental subject that will benefit you in many areas.")
elif Gcse_options == "science":
    print("Excellent! Science is a fascinating subject that opens up many career opportunities.")
elif Gcse_options == "history":
    print("Interesting! History helps us understand the past and its impact on the present.")
elif Gcse_options == "english":
    print("Great choice! English is a valuable subject that enhances communication skills.")
elif Gcse_options == "art":
    print("Wonderful! Art allows for creativity and self-expression.")
elif Gcse_options == "physical education":
    print("Fantastic! Physical Education promotes a healthy lifestyle and teamwork.")
elif Gcse_options == "geography":
    print("Great choice! Geography helps us understand the world and its environments.")
elif Gcse_options == "computer science":
    print("Excellent! Computer Science is a rapidly growing field with many career opportunities.")
elif Gcse_options in ("i dont have any idea", "i don't have any idea", "not sure"):
    print("No worries! It's okay to be unsure about your GCSE options. Take your time to explore different subjects and find what interests you the most.")
elif Gcse_options == "music":
    print("Great choice! Music is a creative subject that develops performance and listening skills.")
else:
    print("Thank you for sharing! You can explore your options and choose what interests you most.")
print("Press enter to exit the program.")
input()
    