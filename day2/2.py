#num_char = len(input('What is your name?'))
# print(type(num_char))

# new_num_char = str(num_char)
#print('Your name has ' + new_num_char + " characters")

a = 123
print(type(a))  # int
b = float(123)
print(type(b))
print(70 + float("100.5"))    # 170.5
print(str(70) + str(100))    # 70100


# Exercise 1
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
# print(type(two_digit_number))
# or    int(two_digit_number[0])

first_digit_num = two_digit_number[0]
second_digit_num = two_digit_number[1]  # int(two_digit_number[1])

result = int(first_digit_num) + int(second_digit_num)
print(result)
####################################


print(2 ** 2)   # 4
print(2 ** 3)   # 8
print(3 * 3 + 3 / 3 - 3)  # 7


# Exercise 2
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# print(type(height))        # str

bmiResult = int(weight) / float(height) ** 2
print(int(bmiResult))
####################################


print(8 / 3)                # 2.6666667
print(int(8 / 3))           # 2
print(round(8 / 3))         # 3
print(round(8 / 3, 2))      # 2.67
print(8 // 3)               # 2

result = 4 / 2
result /= 2
print(result)               # 1.0


score = 0
height = 1.8
isWinning = True
# f-string
print(
    f"Your score is {score}, your height is {height}, you are winning is {isWinning}")


# Exercise 3
# Tim Urban - Your Life in Weeks
# how many days, weeks, months we have left if we live until 90 years old.
# ! There are 365 days in a year, 52 weeks in a year and 12 months in a year. (now no leap year)

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
years_remaining = 90 - int(age)
months_remaining = years_remaining * 12
weeks_reamaining = years_remaining * 52
days_remaining = years_remaining * 365

results = (
    f" You have {years_remaining} years, {months_remaining} months, {weeks_reamaining} weeks, {days_remaining} days left.")
print(results)
####################################


#################################### FINAL PROJECT ####################################
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(
    input("What percentage tip would you like to give? 10, 12, or 15?"))
split = int(input("How many people to split the bill?"))

calc = round(((total * (tip / 100)) + total) / split, 2)
final_amount = "{:.2f}".format(calc)

message = f"Each person should pay {final_amount}"
print(message)
