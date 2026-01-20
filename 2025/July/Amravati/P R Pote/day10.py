
# # class Circle:

# #     def __init__(self, radius):
# #         self.radius = radius

# #     def area(self):
# #         area = (3.14* self.radius * self.radius)
# #         print("Area = ", area)

# #     def perimeter(self):
# #         perm = (3.14 * 2 * self.radius)
# #         # print("Perimeter = ", perm)
# #         print(f"Perimeter = {perm:.3f}")


# # # radius = int(input("Enter the radius of a circle = "))
# # # c1 = Circle(radius)
# # c1 = Circle(5)
# # c1.area()
# # c1.perimeter()


# class Employee:

#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def get_Details(self):
#         print(f"Role = {self.role}")
#         print(f"Departmemt = {self.dept}")
#         print(f"Salary = {self.salary}")
#         print()

# # e1 = Employee("Technical Trainer", "IT", 30_000)
# # e1.get_Details()
        


# # class Engineer:

# #     def __init__(self, name, age, role, dept, salary):
# #         self.name = name
# #         self.age = age
# #         self.role = role
# #         self.dept = dept
# #         self.salary = salary

# #     def get_Details(self):
# #         print(f"Name = {self.name}")
# #         print(f"Age = {self.age}")
# #         print(f"Role = {self.role}")
# #         print(f"Departmemt = {self.dept}")
# #         print(f"Salary = {self.salary}")

# # engg1 = Engineer("Shivam", "42", "Technical Trainer", "IT", 30_000)
# # engg1.get_Details()


# class Engineer(Employee):

#     def __init__(self, name, age, role, dept, salary):
#         super().__init__(role, dept, salary)
#         self.name = name
#         self.age = age

#     def get_Eng_Details(self):
#         print(f"Name = {self.name}")
#         print(f"Age = {self.age}")
#         super().get_Details()

# engg1 = Engineer("Shivam", "42", "Technical Trainer", "IT", 30_000)
# engg1.get_Eng_Details() 




# def add_Sum(x, y):
#     sum = x + y
#     print(sum)

# add_Sum(3, 5)


# sum = lambda x, y: x+y
# print(sum(2, 5))



# def maxOfTwo(x, y):

#     if(x > y):
#         return x
#     else:
#         return y
        
# print(maxOfTwo(10, 40))


# mx = lambda x, y: x if x>y else y
# print(mx(10, 40))



# num = [1, 2, 3, 4, 5]
# doubleFn = lambda x: x*2
# mapD = map(doubleFn, num)
# doubleList = list(mapD)
# print(doubleList)

# num = [1, 2, 3, 4, 5]
# newList = list(map(lambda x: x*2, num))
# print(newList)



# try:
#     a = int(input("Enter = "))
#     for i in range(1, 11):
#         print(a*i)

# except Exception as e:
#     print("Code nahi chala ")
#     print(f"CODE ERROR = {e}")

# else:
#     print("CODE RUNS")

# finally:
#     print("I wil be executed ")

# age = 12

# if(age > 18 or age < 60 ):
#     raise BufferError("Age not within the range")
# # 