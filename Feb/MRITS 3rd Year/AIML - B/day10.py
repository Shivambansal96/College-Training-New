
# # # class College:
# # #     college_name = "MRITS"
# # #     department = "AIML"   # class attribute

# # #     # Default Constructor
# # #     def __init__(self):
# # #         pass
    
# # #     # #parameterized Constructor
# # #     def __init__(self, name, department):
# # #         self.name = name   # Object attribute
# # #         self.department = department   # Object attribute
# # #         print("Adding Students from this College")
        
# # #     def Welcome(self):
# # #         print("Welcome", s1.name+"!")

# # # s1 = College()
# # # print(s1.name, "from", s1.department, "is teaching in", s1.college_name)

# # # s1.Welcome()

# # # # s2 = College("Mohini", "CSE")
# # # # print(s2.name, "from", s2.department, "is teaching in", s2.college_name)







# # class Car:          # Creating a Class
# #     color = "blue"
# #     brand = "mercedes"

# #     def __init__(self):
# #         pass

# #     # @staticmethod
# #     def hello():
# #         print("Cars are Updating")

# # c1 = Car()    # creating an object
# # c2 = Car()    # creating an object
# # c1.hello()

# # # print(c1.color)
# # # print(c1.brand)



# # # class Student:
# # #     dept = "AIML"  # Class Attribute

# # #     def __init__(self, name, marks):
# # #         self.name = name        # object attribute
# # #         self.marks = marks      # object attribute

# # #     def get_avg(self):
# # #         sum = 0
# # #         for i in self.marks:
# # #             sum+=i

# # #         print("The average of", self.name, " marks are ", int(sum /3))

# # # s1 = Student("Shivam", [98, 99, 100])

# # # s1.get_avg()




# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brake = False
#         self.clutch = False
    
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car Started")


# car1 = Car()
# car1.start()



# class Account:

#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.accountNumber = acc

#     def debit(self, amount):
#         self.balance -= amount
    
#     def credit(self, amount):
#         self.balance += amount

#     def print_balance(self):
#         print("Current balance =", self.balance)
        
# person1 = Account(10000, 13424)

# person1.debit(3000)
# person1.credit(30000)
# person1.print_balance()

