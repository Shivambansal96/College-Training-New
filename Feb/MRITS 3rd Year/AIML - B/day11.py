# # # # Private Attribute and Methods
# # # # class Student:

# # # #     name = "Shivam"
# # # #     marks = 90

# # # #     def __init__(self, name, password):
# # # #         self.name = name
# # # #         self.__password = password

# # # #     def hello(self):
# # # #         print("Password inside the class", self.__password)
        
# # # # s1 = Student("Shivam", "Shivam123")
# # # # s1.hello()

# # # # Inheritance
# # # class Car:

# # #     @staticmethod
# # #     def start():
# # #         print("Car Started")

# # #     @staticmethod
# # #     def stop():
# # #         print("Car Stopped")

# # # class ToyotaCar(Car):

# # #     def __init__(self):
# # #         pass

# # # c1 = ToyotaCar()

# # # class newCar(ToyotaCar):

# # #     def __init__(self):
# # #         pass

# # # newCar1 = newCar()
# # # newCar1.start()




# # # # Multiple Inheritance
# # # # class A:
# # # #     name = "Shivam"

# # # #     @staticmethod
# # # #     def start():
# # # #         print("Car Started")

# # # # class B:
# # # #     name = "Bansal"

# # # #     @staticmethod
# # # #     def stop():
# # # #         print("Car Stopped")




# # # # class child(A, B):

# # # #     def __init__(self, name):
# # # #         pass
# # # # c1 = child("name")

# # # # print(c1.name)

# # # # Polymorphism
# # # 1+2         # 3   adding them
# # # "1" + "2"   # 12  concatenating
# # # [1,2,3]+[4, 5, 6] # [1, 2, 3, 4, 5, 6] Merging

# # # print(1+2)
# # # print("1"+"2")
# # # print([1, 2, 3] + [4, 5, 6 ])


# # class Complex:

# #     def __init__(self, real, img):
# #         self.real = real
# #         self.img = img

# #     def showDetails(self):
# #         print(self.real, "i +", self.img, "j")

# #     def __add__(self, num2):
# #         newReal = self.real + num2.real
# #         newImg = self.img + num2.img

# #         return Complex(newReal, newImg)
    


# # num1 = Complex(2, 3)
# # num1.showDetails()

# # num2 = Complex(3, 5)
# # num2.showDetails()


# # num3 = num1.__add__(num2)
# # print(num3.img)
# # print(num3.real)
# # print(num3)





# # # Define a Circle class to create a circle with radius r using the constructor.
# # # Define Area() method of the class which calculates the area of a circle. = (Pie*r*r)
# # # Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle. (2*Pie*r)

# # class Circle:
# #     def __init__(self, radius):
# #         self.radius = radius

# #     def Area(self):
# #         return (22/7)* (self.radius ** 2)
    
# #     def Perimeter(self):
# #         return 2 * (22/7) * self.radius

# # c1 = Circle(25)
# # print("Area =", c1.Area())
# # print("Perimeter =", c1.Perimeter())



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

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "Rs. 80000")

# # e1 = Employee("Accountant", "Finance", 50000)
# # e1.showDetails()

# e1 = Engineer("Shivam", 24)
# e1.showDetails()
# print(e1.name, "with the age of", e1.age, "is an", e1.role, "in the", e1.dept, "Department and earns ", e1.salary)

