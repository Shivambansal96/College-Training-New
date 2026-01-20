

# # class Student:
# #     name = "Shivam Bansal"

# #     def __init__(self):
# #         print("Student Object Created!")

# #     def hello(self):
# #         print("Hello")

# # s1 = Student()
# # print(s1.name)
# # # s1.hello()

# # # print()

# # s2 = Student()
# # print(s2.name)
# # # print(s2)
# # # s2.hello()


# class Student:

#     def __init__(self, name = "Shiv"):
#         self.name = name
#         # s1.name = "Shivam"
#         # s2.name = "Bansal"
    
#     def hello(self):
#         print("Hello", self.name)

# s1 = Student()
# s1.hello()
# # del s1
# # print(s1.name)

# s2 = Student("Shivam")
# s2.hello()
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
        print("Average =", avg)

s1 = Student("Physics", "Chemistry", "Biology", 98, 99, 100)
s1.get_avg()
