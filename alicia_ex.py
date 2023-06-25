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

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 1
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")