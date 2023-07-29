#!/usr/bin/env python 
#Welcome to Band Name Generator
# print("Welcome to the Band Name Generator!")
# city = input("Which city did you grow up in?\n")
# pet = input("What is the name of a pet?\n")
# print("Your band name could be " + city + " " + pet)
# num_ber = len(input("What is your name?"))
# new_num_ber = str(num_ber)
# print("Your name has " + new_num_ber + " characters.")

#Two Digit Sum Calculator Task
# two_digit_number = input("Type a two digit number: ")
# first_digit = two_digit_number [0]
# second_digit = two_digit_number [1]
# result = int(first_digit) + int(second_digit)
# print(result)

# maths

# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3
# print(2 ** 3)

# PEMDAS (left to right)
# ()
# **
# * /
# + -

# print(3 * (3 + 3) / 3 - 3)

# BMI Calculator

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# bmi = int(weight) / float(height) ** 2
# bmi_as_int = int(bmi)
# print(bmi_as_int)

# age = input("What is your current age?")
# age_as_int = int(age)

# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12

# message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
# print(message)

# Tip Calculator

# print("Welcome to the tip calculator.")
# total_bill = float(input("What was the total bill? $"))
# percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
# how_many_people_to_split = int(input("How many people to split the bill? "))
# number = percentage_tip / 100 * total_bill + total_bill
# bill_per_person = number / how_many_people_to_split
# final_amount = round(bill_per_person, 2)
# final_amount = "{:.2f}".format(bill_per_person)
# print(f"Each person should pay ${final_amount}")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("Great! You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5. ")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7. ")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         bill = 12
#         print("Adult tickets are $12. ")

# wants_photo = input("Do you want a photo taken? Y or N")
# if wants_photo == "Y":
#     bill += 3

# print(f"Your final bill is ${bill}!")

# LOVE CALCULATOR

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# combined_string = name1 + name2
# lowercase_string = combined_string.lower()

# t = lowercase_string.count("t")
# r = lowercase_string.count("r")
# u = lowercase_string.count("u")
# e = lowercase_string.count("e")

# true = t + r + u + e

# l = lowercase_string.count("l")
# o = lowercase_string.count("o")
# v = lowercase_string.count("v")
# e = lowercase_string.count("e")

# love = l + o + v + e

# love_score = int(str(true) + str(love))


# if (love_score < 10) or (love_score > 90):
#     print(f"Your love score is {love_score}, you go together like coke and mentos!")

# elif (love_score >= 40) and (love_score <= 50):
#     print(f"Your love score is {love_score}, you are alright together.")

# else:
#     print(f"Your score is {love_score}.")

# Treasure HUNT

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
Q1 = input('There is an intersection that you must cross, as one of the obstacles to get to the    treasure, "left" or "right". You can\'t see the other side of both sides. Which         direction  would you choose?  \n').lower()

if Q1 == "left":
    Q2 = input('You\'ve come to a lake. there is an island n the middle of the lake. Type "wait" to waitfor a boat. Type "swim" to swim across.\n').lower()
    if Q2 == "wait":
        Q3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n").lower()
        if Q3 == "red":
            print("It's a room that is engulfed in flames. Game Over.")
        elif Q3 == "yellow":
            print("You found the room that is full of treasure! You Win!")
        elif Q3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You tripped into a hole and is stuck. Game Over.")