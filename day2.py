# Data types in Python
from pyparsing import nums
project = "jarvis"
version = "2.0"
year = 2024
is_active = True
print(type(project))
print(type(version))
print(type(year))
print(type(is_active))

#if else statement
age =int(input("enter the number:"))
if age >= 18:
    print("eligible for voting")
else:
    print("not eligible for voting")
#elif else statement
marks =int(input("Enter the number:"))
if marks >= 90:
    print("grade a")
elif marks >= 80:
    print("grade b")
elif marks >= 70:
    print("grade c")
elif marks >= 60:
    print("grade d")
elif marks >= 50:
    print("grade e")
else:
    print("Failed")
# Nested if else statement
num = int(input("enter the number:"))
if num >= 18:
    if num <= 90:
        print("eligible for voting and senior citizen")
    else:
        print("age limit exceeded")
else:
    print("not eligible for voting")

# day 2 Task completed
# Task 1
# Even or odd number checker
num =int(input("enter the number:"))
if num % 2 == 0:
    print("even number")
else:
    print("odd number")

# traffic light color checker
color = input("Enter the light color:")
if color =="red":
    print("stop")
elif color =="yellow":
    print("ready")
elif color =="green":
    print("go")
else:
    print("invalid color")

# Leap year checker
year = int(input("Enter the year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")