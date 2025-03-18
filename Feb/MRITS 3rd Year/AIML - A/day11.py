# # # # # # Private Methods and Attributes
# # # # # class Student:

# # # # #     def __init__(self, userName, password):
# # # # #         self.userName = userName
# # # # #         self.__password = password

# # # # #     def showDetails(self):
# # # # #         print("showDetails Method =",self.__password)

# # # # # s1 = Student("ShivamBansal96", "Shivam123")
# # # # # s1.showDetails()
# # # # # # print(s1.userName)
# # # # # # print(s1.__password)


# # # # Inheritance

# # # class Car:
# # #     brand = "mercedes"

# # #     def __init__(self, name):
# # #         self.name = name

# # #         print(self.name)

# # #     @staticmethod
# # #     def start():

# # #         print("Car has Started.")

# # #     @staticmethod
# # #     def stop():
# # #         print("Car has Stopped.")

# # # class Toyota:

# # #     def __init__(self):
# # #         pass

# # #     @staticmethod
# # #     def brake():
# # #         print("Brake is called.")

# # # class Ferrari(Car):
# #     # def __init__(self):
# #     # pass

# # # f1 = Ferrari()
# # # # f1.start()
# # # # f1.brake()
# # # # f1.stop()

# # # # Polymorphism
# # # 1 + 2                       # 3
# # # "1" + "2"                   # 12
# # # [1, 2, 3] + [4, 5, 6]       # [1, 2, 3, 4, 5, 6]

# # # print(1+2)
# # # print("1"+"2")
# # # print([1, 2, 3] + [4, 5, 6])


# # # Complex Numbers

# # class Complex:
# #     def __init__(self, real, img):
# #         self.real = real
# #         self.img = img

# #     def showNumbers(self):
# #         print(self.real,  "i +", self.img, "j")

# #     def __add__(self, num):
# #         newReal = self.real + num.real
# #         newImg = self.img + num.img

# #         print(newReal, "i +", newImg, "j")
# #         # return Complex(newReal, newImg)

# # c1 = Complex(2, 3)
# # c1.showNumbers()

# # c2 = Complex(3, 5)
# # c2.showNumbers()

# # c3 = c1 + c2
# # # c3 = c1.__add__(c2)
# # c3 = c1.__add__(c2)
# # # c3 = c1 + c2
# # # print(c3)


# # Define a Circle class to create a circle with radius r using the constructor.
# # Define Area() method of the class which calculates the area of a circle. = (Pie*r*r)
# # Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle. (2*Pie*r)

# # class Circle:
# #     def __init__(self, radius):
# #         self.radius = radius

# #     def Area(self):
# #         return (22/7)* self.radius ** 2

# #     def Perimeter(self):
# #         return 2 * (22/7) * self.radius

# # c1 = Circle(25)
# # print(c1.Area())
# # print(c1.Perimeter())




# # Define an Employee class with attribute role, department & Salary. This class also has a showDetails() method.
# # Create an Engineer class that inherits properties from Employee & has additional attributes : name & age.

# class Employee:

#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("Role =", self.role)
#         print("Department =", self.dept)
#         print("Salary =", self.salary)

# # e1 = Employee("Accountant", "Finance", 40000)
# # e1.showDetails()

# class Engineer(Employee):

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#         super().__init__("Technical Trainer", "IT Department", "Rs 80000")

#         print(self.name, "with the age of", self.age, "has certain details :-")

# e1 = Engineer("Shivam", 24)
# e1.showDetails()





