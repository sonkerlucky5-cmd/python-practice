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


           