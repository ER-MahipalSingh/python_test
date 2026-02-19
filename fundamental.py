print("Welcome to the Interactive Personal Date Collector")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
favourite_number = int(input("Enter your favourite number: "))

print("Name: ", name, "(type: ", type(name),")", "(Memory Address: ", id(name),")")
print("Age: ", age, "(type: ", type(age),")", "(Memory Address: ", id(age),")")
print("height: ", height, "(type: ", type(height),")", "(Memory Address: ", id(height),")")
print("Favourite_number: ", favourite_number, "(type: ", type(favourite_number),")", "(Memory Address: ", id(favourite_number),")")

birth_year=2026-age
print("Birth year acroding to age: ", birth_year)

print("Tahnks for using the Personal Data Collector. Goodbye!")
