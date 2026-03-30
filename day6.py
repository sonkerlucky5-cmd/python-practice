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
def greet(name):
    print(f"Hello, {name}!")