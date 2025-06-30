# class Student:
#     college_name = "DKTE"

#     def __init__(self, name , age):
#         self.name = name
#         self.age = age

#     def student_info(self):
#         print(f"Name = {self.name}")
#         print(f"Age = {self.age}")
#         print(f"College = {self.college_name}")
#         print("------------")
        

# s1 = Student("Shivam", 24)
# # s1.student_info()

# print(s1.brand)
# print(s1.name)

# s2 = Student("Arjun", 45)
# # s2.student_info()



# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     @staticmethod # ignores the compulsion to add
#                                 #  self as a parameter

#     def welcome_msg():
#         print(f"Welcome Student")
    
#     def get_avg(self):
        
#         sum = 0
#         for i in self.marks:
#             sum += i
#         avg = sum / 3
#         return avg

# s1 = Student("Shivam", [98, 99, 97])
# # ans = s1.get_avg()
# s1.welcome_msg()

# # print(f"{s1.name}'s average Score is {ans}")
        
# # s2 = Student("Arjun", [99, 100, 10])
# # ans = s2.get_avg()

# # print(f"{s2.name}'s average Score is {ans}")
        

# class Student:
#     name = "anonymous"

#     def __init__(self, name):
#         self.name = name

# s1 = Student()


# class Student():
#     name = "Shivam"
#     age = 0000000

#     # def __init__(self):
#     #     # self.name = "Karan"
#     #     self.__class__.name = "Karan"

#     @classmethod
#     def changeName(cls):
#         cls.name = "Karan"
#         cls.age = 24
# s1 = Student()
# print(s1.name, s1.age)




# class Car:

#     def __init__(self):
#         self.acc = False
#         self.clutch = False
#         self.brake = False
        
#     @staticmethod
#     def start():
#         print("has Started...")

#     @staticmethod
#     def stop():
#         print("has Stopped...")
    
#     def checkInfo(self, name):
#         self.name = name
#         print(f"{name}.... {self.start()}")

# c1 = Car()
# c1.checkInfo("BMW")
# c2 = Car()


# class Account:

#     def __init__(self, accNo, acc_pass):
#         self.accNo = accNo
#         self.__acc_pass = acc_pass

#     def checkPass(self):
#         print(self.__acc_pass)

# a1 = Account("12345", "Shivam")
# print(a1.accNo)

# a1.checkPass()




# class Account:

#     def __init__(self, accNo, acc_pass, balance):
#         self.accNo = accNo
#         self.acc_pass = acc_pass
#         self.__balance = balance

#     def check_pass(self):
#         print(f"Your password is {self.acc_pass}")

#     def check_bal(self):
#         print(f"Total Amount is Rs {self.__balance}")


#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"Rs {amount} has been credited.")

#     def withdraw(self, amount):
#         if(self.__balance > 0):
#             self.__balance -= amount
#             print(f"Rs {amount} has been debited.")

# a1 = Account("143801000115559", "Shivam", 30_000)

# a1.deposit(20_000)
# a1.withdraw(40_000)
# a1.check_bal()


# # SINgle LEvel Inheritance
# class Car:

#     @staticmethod
#     def start():
#         print("Car has started...")

#     @staticmethod
#     def stop():
#         print("Car has stoppped...")

# class ToyotaCar(Car):
#     name = "Toyota"


# t1 = ToyotaCar()
# t1.start()


# # Multi-Level Inheritance
# class Animal:

#     @staticmethod
#     def eat():
#         print("Animals eat something")

# class Herbivore(Animal):

#    def __init__(self):
#         pass

# class Carnivore(Animal):

#     def __init__(self):
#         pass


# h1 = Herbivore()
# h1.eat()

# c1 = Carnivore()
# c1.eat()


# # Multiple Inheritance

# class Father:

#     @staticmethod
#     def earnMOney():
#         print("earn money")

# class Mother:

#     @staticmethod
#     def showLove():
#         print("show love")


# class Child(Father, Mother):

#     def __init__(self):
#         pass

# c1 = Child()
# c1.showLove()
# c1.earnMOney()



# print(3+5) #8
# print("hello " "world") #hello world
# print([34, 644, 462] + [342,3522,5322]) # merge


# class Complex:

#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def get_output(self):
#         print(f"{self.img}i + {self.real}j")

#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

# c1 = Complex(3, 2)
# c1.get_output()

# c2 = Complex(4, 5)
# c2.get_output()

# c3 = c1 + c2
# c3.get_output()


class Employee:
    def __init__(self, role, dept, salary):
        self.role = role        
        self.dept = dept        
        self.salary = salary

    def showDetails(self):
        print(f"Role = {self.role}")
        print(f"Department = {self.dept}")
        print(f"Salary = {self.salary}")

class Engineer(Employee):
    def __init__(self, name , age, role, dept, salary):
        super().__init__(role, dept, salary)
        self.name = name
        self.age = age

    def showNewDetails(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        super().showDetails()

e1 = Employee("Technical Trainer", "IT", 50_000)
# e1.showDetails()

eng1 = Engineer("Shivam", 24, "SDE", "Testing", 75_000)
eng1.showNewDetails()
