
class Student:
    name = "Shivam Bansal"
    age = 26

    def hello(self):
        print(f"self = {self}")

s1 = Student()
print(f"S1 = {s1}")
s1.hello()

print("----------------")
s2 = Student()
print(f"S2 = {s2}")
s2.hello()