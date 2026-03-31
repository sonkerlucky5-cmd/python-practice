# string 
str = "Lucky Sonker"
print(str)
# indexing characters
print("first character:", str[0])
print("last character:", str[1])
# slicing
print(str[0:5])
print(str[9:12])
# Length of string
print("Length of string:", len(str))
# Count characters
text = input("enter the string: ")
char = input("enter the character to count: ")
count = text.count(char)        
print(f"The character '{char}' appears {count} times in the string.")

# functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
