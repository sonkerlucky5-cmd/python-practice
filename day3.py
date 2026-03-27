# for loops
for i in range(100):
    print(i)    
# for loops second example
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# while loop 
password = "1234"

while True:
    user = input("Enter password: ")
    if user == password:
        print("Access granted")
        break
    else:
        print("Wrong password")