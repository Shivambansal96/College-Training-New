
# # # # # # class Circle:

# # # # # #     def __init__(self, radius):
# # # # # #         self.radius = radius

# # # # # #     def AreaOfCircle(self):
# # # # # #         area = (22/7) * self.radius ** 2
# # # # # #         # print(area)
# # # # # #         return area

# # # # # #     def perimeter(self):
# # # # # #         per = (22/7) * self.radius * 2
# # # # # #         # print(per)
# # # # # #         return per

# # # # # #     def displayResult(self):
# # # # # #         res = self.AreaOfCircle()
# # # # # #         print(res)
# # # # # #         # print(f"Area = {self.AreaOfCircle()}")
# # # # # #         print(f"Perimeter = {self.perimeter()}")

# # # # # # c1 = Circle(3)
# # # # # # c1.displayResult()



# # # # # class Student:

# # # # #     @staticmethod
# # # # #     def hello():
# # # # #         print("Hello")    

# # # # # s1 = Student()
# # # # # s1.hello()


# # # # class Car:

# # # #     def __init__(self, brand, acc, clutch, brake):
# # # #         self.brand = brand
# # # #         self.acc = acc
# # # #         self.clutch = clutch
# # # #         self.brake = brake

# # # #     def start(self):
# # # #         self.acc = True
# # # #         self.clutch = True
# # # #         self.brake = False
# # # #         print(f"{self.brand} has Started")

# # # #     def stop(self):
# # # #         self.acc = False
# # # #         self.clutch = True
# # # #         self.brake = True
# # # #         print(f"{self.brand} has Stopped")

# # # # c1 = Car("BMW", False,False,False)
# # # # c1.start()
# # # # c1.stop()


# # # class Student:

# # #     def __init__(self, userName, AcPass):
# # #         self.userName = userName
# # #         self.__AcPass = AcPass

# # #     def __displayOutput(self):
# # #         print(self.userName)
# # #         print(self.__AcPass)

# # #     def hello(self):
# # #         self.__displayOutput()

# # # s1 = Student("Shivambansal96", "Shivam123")
# # # s1.hello()
# # # # s1.__displayOutput()

# # # # print(s1.userName)
# # # # print(s1.__AcPass)



# # class Account:

# #     def __init__(self, accNo, bal):
# #         self.accNo = accNo
# #         self.balance = bal


# #     def debit(self, amount):
# #         if(self.balance <= amount):
# #             print("Insufficent Balance.")

# #         else:
# #             self.balance = self.balance - amount
# #             print(f"Rs. {amount} debited.")

# #     def credit(self, amount):
# #         self.balance = self.balance + amount
# #         print(f"Rs. {amount} credited.")

# #     def getBalance(self):
# #         print(f"Balance = Rs. {self.balance}")

# # a1 = Account("Shivam12345", 5000)

# # a1.debit(10000)
# # a1.credit(2000)
# # a1.getBalance()


# # class Shape:
# #     color = "red"
# #     type = "blend"

# # class Circle:
# #     OK = "ok"

# # class Triangle(Shape, Circle):

# #     def __init__(self):
# #         pass


# # tt1 = Triangle()
# # print(tt1.color)
# # print(tt1.OK)


# # class Equilateral_Triangle(Triangle):

# #     def __init__(self):
# #         pass

# # class Right_angled_Triangle(Triangle):

# #     def __init__(self):
# #         pass


# # # t1 = Triangle()
# # # print(t1.color)

# # t1 = Equilateral_Triangle()
# # print(t1.color)

# # r1 = Right_angled_Triangle()
# # print(r1.color)


# class Shape:
#     def __init__(self, color, type):
#         self.color = color
#         self.type = type
#         print("Shape")

# class Circle(Shape):

#     def __init__(self, color, type):
#         super().__init__(color, type)

    
# s1 = Shape("red", "blend")
# print(s1.color)
# print(s1.type)

# c1 = Circle("green", "hiugyftdrsghjk")
# print(c1.color)
# # print(c1.type)



# a = 5
# b = 10

# print(a + b)

c = "Hello"
# d = "World"
d = 3

print(c * d)

# a = [76, 98, 8]
# b = [9976, 798, 88]

# print(a + b)