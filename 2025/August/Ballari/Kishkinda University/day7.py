
# class Student:

#     def __init__(self, name="anonymous"):
#         self.name = name

#     def hello(self):
#         print(f"Hello {self.name}!!!")

# s1 = Student("Shivam")
# # del s1.name
# # del s1
# # s1.hello()
# print(s1.name)



# # # print("----------------")
# # s2 = Student("Shiv")
# # print(s2.name)
# # s2.hello()




# class Student:

#     def __init__(self, name, m1, m2, m3):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def get_avg(self):
#         avg = (self.m1 + self.m2 + self.m3) // 3
#         print(avg)

# s1 = Student("Shivam", 40, 45, 50)
# s1.get_avg()



# class Circle:

#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         # area = (22/7) * self.radius * self.radius
#         area = (22/7) * self.radius ** 2
#         print(f"Area = {area}")

#     def get_perimeter(self):
#         perimeter = (22/7) * 2 * self.radius
#         print(f"Perimeter = {perimeter}")

# c1 = Circle(5)
# c1.get_area()
# c1.get_perimeter()


# class Circle:

#     def __init__(self, radius):
#         self.r = radius

#     def get_area(self):
#         area = (22/7) * self.r ** 2
#         print(f"ARea = {area}")

#     def get_perimeter(self):
#         perimeter = (22/7) * self.r * 2
#         print(f"Perimeter = {perimeter}")

# c1 = Circle(9)
# c1.get_area()
# c1.get_perimeter()



# class Student:

#     @staticmethod
#     def hello():
#         print("Hello World")

# s1 = Student()
# s1.hello()


# class Car:

#     def __init__(self):
#         self.combustion = False
#         self.petrolTransfer = False
#         self.engine = False

#     def start(self):

#         self.combustion = True
#         self.petrolTransfer = True
#         self.engine = True
#         print("Car has Started...")        

#     def stop(self):

#         self.combustion = False
#         self.petrolTransfer = False
#         self.engine = False
#         print("Car has Stopped...")        



# c1 = Car()
# c1.start()
# c1.stop()



# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

# class Dog:

#     def noise(self):
#         print("Dog Barks")

#     # def sound(self):
#     #     print("Dog Barks")

# class Cat:

#     def sound(self):
#         print("Cat Meows")

# a1 = Animal() # # This will give an error since abstract class cannot be created as an object, it cannot become  areal world entity

# d1 = Dog()
# d1.noise()

# c1 = Cat()
# c1.sound()


# class Student:
#     __name = "Shivam"

#     def __init__(self):
#         print(self.__name)


# s1 = Student()
# # print(s1.__name)


# class Bank:

#     def __init__(self, name, AcNum, AcPass):
#         self.name = name
#         self.AcNum = AcNum
#         self.__AcPass = AcPass

#     # @staticmethod
#     # def hello():
#     #     print("Hello World")

#     # def get_name(self):
#     #     print(self.name)
    
#     def __get_Password(self):
#         print(f"Account Password = {b1.__AcPass}")



# b1 = Bank("Shivam", 14380100115559, "Shivam123")
# # b1.get_name()


# # b2 = Bank("Bansal", 4242, "grqwhgq")
# # b2.get_name()
# # Bank.get_name(b2)


# print(f"Account Number = {b1.AcNum}")
# # print(f"Account Password = {b1.__AcPass}")
# b1.__get_Password



# class Bank:

#     def __init__(self, AcNum, AcPass):
#         self.AcNum = AcNum
#         self.__AcPass = AcPass

#     def get_Output(self):
#         self.__get_Password()
#         print(1)

#     def __get_Password(self):
#         print(f"Account Password = {b1.__AcPass}")
#         print(2)

# b1 = Bank(14380100115559, "Shivam123")
# print(f"Account Number = {b1.AcNum}")
# # print(f"Account Password = {b1.__AcPass}")
# # b1.__get_Password()
# b1.get_Output()
# print(3)



# class Account:
#     def __init__(self, accNo, balance):
#         self.bal = balance
#         self.accNum = accNo

#     def debit(self, amount):
#         if(self.bal >= amount):
#             self.bal -= amount
#             print(f"Rs {amount} has been debited.")
#         else:
#             print("Insufficient Balance")
#             self.get_balance()

#     def credit(self, amount):
#         self.bal += amount
#         print(f"Rs {amount} has been credited.")

#     def get_balance(self):
#         print(f"Total Balance = Rs {self.bal}")


# a1 = Account(14380100115559, 3_00_000)
# # print(a1.accNum)
# # print(a1.bal)
# a1.debit(10_00_000)
# print()
# a1.credit(50_000)



