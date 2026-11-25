# Mini Project - Personalize greeting program 

#datetime built-in module used to work with date & time
from datetime import datetime


#step 1 : Ask for User Details
name = input("What's your name?")

birth_year = int(input("What's Your Birth Year?"))

#Extracts year and month 
current_year = datetime.now().year

# calculate age = present year - birth year
age = current_year - birth_year

color = input("What's your favorite color?")

#step 2 : personalize greeting
print("\n-------Personalize Greeting------")
print("Hello, {}!" .format(name))
print(f"Your Favourite Colour {color}")
print(f"you are {age} years old")


