

# # # # class Shape:
# # # #     color = "red"
# # # #     def printing_Something(self):
# # # #         print("Hello I am a Shape")

# # # # class Triangle(Shape):

# # # #     def __init__(self):
# # # #         pass

# # # # class Circle(Shape):

# # # #     def __init__(self):
# # # #         pass

# # # # class Equilateral_Triangle(Triangle):

# # # #     def __init__(self):
# # # #         pass

# # # # s1 = Shape()
# # # # print(s1.color)
# # # # s1.printing_Something()

# # # # t1 = Triangle()
# # # # print(t1.color)
# # # # t1.printing_Something()

# # # # e1 = Equilateral_Triangle()
# # # # e1.printing_Something()
# # # # print(e1.color)

# # # # c1 = Circle()
# # # # print(c1.color)


# # # # class A:
# # # #     var= "A"

# # # # class B:
# # # #     newVar = "B"

# # # # class C(A, B):
# # # #     color = "C"

# # # # c1= C()
# # # # print(c1.var)
# # # # print(c1.newVar)
# # # # print(c1.color)   


# # # class Employee:

# # #     def __init__(self, role, dept, salary):
# # #         self.role = role
# # #         # e1.role = "Account Manager"
# # #         self.dept = dept
# # #         self.salary = salary

# # #     def showDetails(self):
# # #         print(f"Role = {self.role}")
# # #         print(f"Department = {self.dept}")
# # #         print(f"Salary = {self.salary}")

# # # e1 = Employee("Account Manager", "Finance", 30_000)
# # # # e1.showDetails()


# # # # # # BASIC DEFAULT thing without INHERITANCE
# # # # class Engineer:

# # # #     def __init__(self, name, age, role, dept, salary) :
# # # #         self.name = name
# # # #         self.age = age
# # # #         self.role = role
# # # #         self.dept = dept
# # # #         self.salary = salary

# # # #     def showDetails(self):
# # # #         print(f"Name = {self.name}")
# # # #         print(f"Age = {self.age}")
# # # #         print(f"Role = {self.role}")
# # # #         print(f"Department = {self.dept}")
# # # #         print(f"Salary = {self.salary}")

# # # # engg1 = Engineer("Shivam", 25, "Technician", "IT", 50_000)
# # # # engg1.showDetails()


# # # # # # WITH INHERITANCE and SUPER KEYWORD

# # # class Engineer(Employee):

# # #     def __init__(self, name, age, role, dept, salary):
# # #         self.name = name
# # #         self.age = age
# # #         super().__init__(role, dept, salary)

# # #     def showDetails(self):
# # #         print(f"Name = {self.name}")
# # #         print(f"Age = {self.age}")
# # #         super().showDetails()

# # # engg1 = Engineer("Shivam", 25, "Technical Trainer", "IT", 1_00_000)
# # # engg1.showDetails()



# # # Operator is same but OPERANDS are changing
# # # print(2 + 4)
# # # print("2" + "4")
# # # print([2] + [4])

# # # print(2 - 4)
# # # print(2 - "4")
# # # print({2, 4} - {3, 4})

# # # print(2 * 3)
# # # print("2" * 3)
# # # print("2" * "3")

# # # class Complex:

# # #     def __init__(self, real, img):
# # #         self.real = real
# # #         self.img = img
    
# # #     def showNum(self):
# # #         print(f"{self.real} + {self.img}j")

# # #     def __add__(self, new):
# # #         newReal = self.real + new.real
# # #         newImg = self.img + new.img
# # #         return Complex(newReal, newImg)

# # # c1 = Complex(5, 3)
# # # c1.showNum()

# # # c2 = Complex(2, 8)
# # # c2.showNum()

# # # # c3 = c1.add(c2)
# # # # c3.showNum()

# # # c3 = c1 + c2
# # # # print(c3)
# # # c3.showNum()



# # class Complex:

# #     def __init__(self, real, img):
# #         self.real = real
# #         self.img = img
    
# #     def showNum(self):
# #         if(self.real > 0 and self.img > 0):
# #             print(f"{self.real} + {self.img}j")
# #         elif(self.img < 0):
# #             print(f"{self.real} - {-self.img}j")
            

# #     def __add__(self, new):
# #         newReal = self.real + new.real
# #         newImg = self.img + new.img
# #         return Complex(newReal, newImg)


# #     def __sub__(self, new):
# #         newReal = self.real - new.real
# #         newImg = self.img - new.img
# #         return Complex(newReal, newImg)

# # c1 = Complex(5, 3)
# # c1.showNum()

# # c2 = Complex(2, 8)
# # c2.showNum()

# # # c3 = c1.add(c2)
# # # c3.showNum()

# # c4 = c1 - c2
# # # print(c3)
# # c4.showNum()


# import string
# import random

# n = int(input("Enter the length of your password = "))
# allCharacters = string.ascii_letters + string.digits + "!@#$%^&?-_"

# randomPass = ""
# for i in range(n):
#     randomCharacter = random.choice(allCharacters)
#     randomPass += randomCharacter

# print(randomPass)
