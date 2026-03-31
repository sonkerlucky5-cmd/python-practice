# file handling write using with statement
with open("file1.txt", "w") as file:
    file.write("day 1 start coding.\n")
    file.write("day 2 continue coding.\n")
    file.write("day 3 complete the project.\n")
# file handling read using with statement
with open("file1.txt", "r") as file:
    content = file.read()
    print(content)
# file handling append using with statement
with open("file1.txt", "a") as file:
    file.write("day 4 review the code.\n")
# file handling write and read using with statement
with open("file1.txt", "w+r") as file:
    file.write("day 5 start testing.\n")
    file.seek(0)  # Move the cursor to the beginning of the file
    content = file.read()
    print(content)
    # Step 1: Write initial data
with open("students.txt", "w") as f:
    f.write("Name: Lucky, Age: 20\n")
    f.write("Name: Rahul, Age: 22\n")

# Step 2: Append new data using user input
n = int(input("How many students you want to add: "))

with open("students.txt", "a") as f:
    for i in range(n):
        name = input("Enter name: ")
        age = input("Enter age: ")
        f.write(f"Name: {name}, Age: {age}\n")

# Step 3: Read and display all data
print("\nAll Students Data:\n")

with open("students.txt", "r") as f:
    for line in f:
        print(line.strip())