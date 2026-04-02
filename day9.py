# Exception Handling Example (Beginner to Advanced)

def divide_numbers():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Invalid input (enter numbers only)")
    finally:
        print("Division operation complete\n")


def file_read():
    try:
        with open("data.txt", "r") as f:
            print("File Content:")
            print(f.read())
    except FileNotFoundError:
        print("Error: File not found\n")


def list_access():
    try:
        nums = [10, 20, 30]
        index = int(input("Enter index (0-2): "))
        print("Value:", nums[index])
    except IndexError:
        print("Error: Index out of range")
    except ValueError:
        print("Error: Enter valid number\n")


def custom_exception():
    try:
        age = int(input("Enter your age: "))
        if age < 18:
            raise Exception("You are not eligible")
        print("You are eligible")
    except Exception as e:
        print("Error:", e, "\n")


def multiple_exceptions():
    try:
        num = int(input("Enter number: "))
        print(100 / num)
    except (ZeroDivisionError, ValueError) as e:
        print("Error occurred:", e, "\n")


def main():
    print("=== Exception Handling Demo ===\n")

    divide_numbers()
    file_read()
    list_access()
    custom_exception()
    multiple_exceptions()

    print("Program finished safely")


if __name__ == "__main__":
    main()