
# # class Student():
# #     name = "Shivam Bansal" # Class Data

# #     def __init__(self):
# #         print("Student Object Created!")   # Created by default of we dont create it.
        
# #     #  Hello Method created.
# #     def hello(self):
# #         print(self)

# # # Object Created
# # s1 = Student() # Creating Constructor
# # print(s1.name)



# # # s1.hello()

# # # print(s1.name)
# # # s1.hello()

# # # s2 = Student()
# # # print(s2)




# class Student():
#     # name = "Shivam Bansal" # Class Data

#     def __init__(self, name = "Shiv"):
#         self.name = name
#         print(f"Student Object Created!")  
        
#     def hello(self):
#         # print(self)
#         print("OK")

# s1 = Student() 
# Student.hello(s1)
# s1.hello()
# # print(s1.name)



# # s2 = Student("Bansal")
# # print(s2.name)


class Student:

    def __init__(self, sub1, sub2, sub3, m1, m2, m3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def get_avg(self):
        avg = (self.m1 + self.m2 + self.m3) // 3
        print(avg)


s1 = Student("S", "A", "P", 99, 98, 100)

s1.get_avg()