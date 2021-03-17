# 1-exercise
#print("Day 1 - Python Print Function")
#print("The function is declared like this: ")
#print("print('what to print')")
#print("Hello World!\nHello Gabcsika!\nHello Python!")
#print("Hello" + " " + "Gabcsi")

# 2-exercise
#print("Day 1 - String Manipulation")
#print('String Concatenation is done with the "+" sign.')
#print('e.g. print("Hello " + "world")\nNew lines can be created with a backslash and n.')

# 9
#print("Hello " + input("What is your name?"))

# 3-exercise
#print(len(input("What is your name?")))

# 11
#name = input("What is your name?")
#length = len(name)
# print(length)
"""
# 4-exercise
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
c = a
a = b
b = c

# Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# 13
user_name = input("What is your name?")
"""


# day 1 - final project
# 1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in.
# 3. Ask the user for the name of a pet.
# 4. Combine the name of their city and pet and show them their band name.
# 5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

print("Welcome to the Band Name Generator!")
city = input("What's name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be: " + city + " " + pet)
