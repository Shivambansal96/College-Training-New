# # # # class Student:                      # Creating a class
# # # #     college_name = "MRITS"          # Class Attribute(data, i.e., Variable)
# # # #     department = "AIML"
# # # #     section = "A"
# # # #     name = "Anonymous"

# # # #     # Default Constructor
# # # #     def __init__(self):
# # # #         print("OOP CONCEPT!!!")

# # # #     # Parameterized Constructor
# # # #     def __init__(self, name , marks):
# # # #         self.name = name           # Object Attribute(data, i.e., Variable)
# # # #         self.marks = marks
# # # #         print(self)

# # # #     def welcome(self):
# # # #         print("Welcome", self.name)

# # # # s1 = Student()
# # # # s1.welcome()
# # # # # print(s1)


# # # # # print(s1.name, "from", s1.department, "got", s1.marks, "marks, studying in the", s1.college_name, "College" )

# # # # # s2 = Student("Shivam", 95)
# # # # # print(s2.name, "from", s2.department, "got", s2.marks, "marks, studying in the", s2.college_name, "College" )

# # class Car:
# #     color = "blue"
# #     brand = "mercedes"
# #     price = "20L"

# #     @staticmethod
# #     def checking():
# #         print("Price of", c1.brand, "is", c1.price)

# # c1 = Car()
# # c1.checking()


# # # # Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

# # # class Student:

# # #     def __init__(self, name, marks):
# # #         self.name = name
# # #         self.marks = marks

# # #     def get_avg(self):
# # #         sum = 0
# # #         for i in self.marks:
# # #             sum+=i
        
# # #         print(sum//3)


# # # s1 = Student("Shivam", [98, 99, 100])
# # # # print(s1.name, "got", s1.marks, "in the three Subjects")
# # # s1.get_avg()



# # #Abstraction example

# # class Car:

# #     def __init__(self):
# #         self.accelerator = False
# #         self.brake = False
# #         self.clutch = False

# #     def start(self):
# #         self.accelerator = True
# #         self.clutch = True
# #         print("Car Started")


# # c1 = Car()
# # c1.start()

# class Account:

#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.accountNumber = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Balance after Amount debited =", self.balance)
    
#     def credit(self, amount):
#         self.balance += amount
#         print("Balance after Amount credited =", self.balance)

    
#     def printing_bal(self):
#         print("Current Balance =", self.balance)

# person1 = Account(10000, 123452)
# person1.debit(3000)
# person1.credit(30000)

# person1.printing_bal()

# class Student:
#     name = "Shivam"
#     name = "Shivam"
#     name = "Shivam"

# s1 = Student()
# del s1
# print(s1.name)