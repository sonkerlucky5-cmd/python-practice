# first revision test of day 10
for i in range(1,21):
    print(i)
    if i % 3 == 0 and i % 5 == 0:
        print("AI enginner")
    elif i % 3 == 0:   
        print("AI")
    elif i % 5 == 0:    
        print("enginner")
    else:
        print(i)
# second revision test of day 10
class ai_engineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
# object create 
Engineer1 = ai_engineer("Alice", 30)
Engineer2 = ai_engineer("Bob", 25)
Engineer3 = ai_engineer("Charlie", 35)
Engineer4 = ai_engineer("David", 28)
Engineer5 = ai_engineer("Eve", 32)
Engineer6 = ai_engineer("Frank", 27)
Engineer7 = ai_engineer("Grace", 29)
# introduce the engineers
Engineer1.introduce()   
Engineer2.introduce()
Engineer3.introduce()
Engineer4.introduce()
Engineer5.introduce()
Engineer6.introduce()
Engineer7.introduce()


