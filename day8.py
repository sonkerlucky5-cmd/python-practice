# class & object student:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("name", self.name)
        print("age", self.age)
s1 = Student("Lucky", 20)
s1.show()

# inheritence oops concept
class Animal:
    def eat(self):
        print("eat")
class dog(Animal):
    def bark(self):
        print("bark")

d1 = dog()
d1.eat()
d1.bark()

# polymorphism oops concept
class Bird:
    def fly(self):
        print("fly")

class Penguin(Bird):
    def fly(self):
        print("penguin cannot fly")

b1 = Bird()
b1.fly()    
p1 = Penguin()
p1.fly()    
# encapsulation oops concept
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print("Balance:", account.get_balance())

# abstraction oops concept
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
c1 = Circle(5)
print("Area of circle:", c1.area()) 

