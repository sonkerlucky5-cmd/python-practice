print("my first program in publish Github")
print("Hello github")

#Arithmatic operation
a = 5
b = 6
print("addition", a + b)
print("subtraction", a - b)
print("multiplication", a * b)
print("divide", a / b)
print("power", a ** b)

#Arithmatic operation new program advanced level

print("\n=====Arithmatic operation=====")
a = int(input("Enter the First:"))
b = int(input("Enter the Second:"))
print("addition =",a + b)
print("Subtraction =",a - b)
print("multiplication =",a * b)
if b != 0:
    print("division =",a / b)
else:
    print("division not possible(b = 0)")
    # Extra modules 
    print("module =", a % b)
    print("power =",a ** b)
    print("Floor Division =", a // b)
    # Even and odd cheaker 
    num =  int(input("Enter the number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("odd")
    # positive , negative , zero 
    num = int(input("Enter the number: "))
    if num > 0:
        print("positive")
    elif num < 0:
        print("Negative")
    else:
        print("zero")
    # Student Result system 
    print("------Student Result System------")

    name = input("Enter Student name: ")

    m1 = int(input("Enter the marks of subject 1: "))
    m2 = int(input("Enter the marks of subject 2: "))
    m3 = int(input("Enter the marks of subject 3: "))
    m4 = int(input("Enter the marks of subject 4: "))
    m5 = int(input("Enter the marks of subject 5: "))
    total = m1 + m2 + m3 + m4 + m5 
    percentage = total / 5
    print("\nName:", name) 
    print("Total marks:", total)
    print("percentage:", percentage)
    if percentage >= 40:
        print("result: Pass")
    else:
        print("result: Fail")
    if percentage >= 80:
        print("grade A")
    elif percentage >= 60:
        print("grade B")
    elif percentage >= 40:
        print("grade C")
    else:
        print("Failed")
    # Loops 
    for i in range(0,90):
        print(i)
    def check_even_odd(nums):
        if nums % 2 == 0:
            print("even")
        else:
            print("odd")
        check_even_odd
    # List 
    