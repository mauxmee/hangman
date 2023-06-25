#!/usr/bin/env python3
# input() will get use input in the console
# Then print() will print the word "Hello" and the user input
# print("Hello " + input("What is your name?") + "!")
# name = "Jack"
# print(name)

# name = "Angela"
# print(name)


# name = input("What is your name?")
# length = len(name)
# print(length)

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#   print(f"Your bmi is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your bmi is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your bmi is {bmi}, you are overweight.")
# elif bmi < 35:
#   print(f"Your bmi is {bmi}, you are obese.")
# else:
#   print(f"Your bmi is {bmi}, you are clinically obese.")



# year = int(input("Which year do you want to check?"))


# if year % == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N.")
  if wants_photo == "Y":
    bill += 3

  print(f"Your final bill is {bill}.")

else:
  print("Sorry, you have to grow taller before you can ride.")