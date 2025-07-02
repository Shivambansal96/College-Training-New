


# class Student: # Class Creation

#     def __init__(self, name): # As soon as the contructor is created
#         self.name = name  # s1.name = Shivam & s2.name = Shiv
#         # print(f"Object {self.name} created")
#         self.welcome()

#     def welcome(self):
#         print("welcome", self.name)


# s1 = Student("Shivam") # Object Creation
# print(f"s1 = {s1.name}")

# s2 = Student("Shiv") # Object Creation
# print(f"s2 = {s2.name}")

# del s1.name
# print(s1.name)

# class Student:

#     def __init__(self, name, marks1, marks2, marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3

#     def get_avg(self):
#         sum = self.marks1 + self.marks2 + self.marks3
#         avg = sum / 3
#         print(avg)

# s1 = Student("Shivam", 98, 99, 97)
# s1.get_avg()
        


# class Student:

#     @staticmethod
#     def welcome():
#         print("Welcome")

# s1= Student()
# s1.welcome()


# class Car:

#     @staticmethod
#     def start():
#         clutch = True
#         acc = True
#         brake = False
#         print("Car has started...")

#     @staticmethod
#     def stop():
#         clutch = True
#         acc = False
#         brake = True
#         print("Car has stopped...")


# Ferrari = Car()
# Ferrari.start()
# Ferrari.stop()

# from abc import ABC, abstractmethod

# class Car(ABC):
   
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass
    
# class Toyota(Car):

#     def __init__(self, acc, brake, clutch):
#         self.acc = acc
#         self.clutch = clutch
#         self.brake = brake

#     @staticmethod
#     def run():
#         print("Car is running")

#     def start(self):
#         self.acc = True
#         self.clutch = True
#         self.brake = False
#         print("Car has started...")

#     def stop(self):
#         self.acc = False
#         self.clutch = True
#         self.brake = True
#         print("Car has stopped...")


# t1 = Toyota(False, False, False)
# t1.run()
# t1.start()
# t1.stop()

# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def speak(self):
#         print("CANT TALK")

# class Horse(Animal):

#     def run(self):
#         print("runs")

#     def speak(self):
#         # return super().speak()
#         print("CANT SPEAK")

# h1 = Horse()
# h1.speak()




# class Account:
#     def __init__(self, userName, password):
#         self.__userName = userName
#         self.__password = password

#     def getData(self):
#         self.__get_Details()
    
#     def __get_Details(self):
#         print(f"You Username is {self.__userName}")
#         print(f"You Password is {self.__password}")


# a1 = Account("Shivambansal96", "Shivam12345")
# a1.getData()


# class Account:

#     def __init__(self, accNo, accPass, balance):
#         self.accNo = accNo
#         self.accPass = accPass
#         self.balance = balance
    
#     def credit_Amount(self, amount):
#         self.balance += amount
#         print(f"Credited Rs.{amount}")
#         print(f"Balance remaining: Rs {self.balance}")

#     def debit_Amount(self, amount):
#         self.balance -= amount
#         print(f"Debited Rs.{amount}")
#         print(f"Balance remaining: Rs {self.balance}")

#     def get_balance(self):
#         print(f"Total Balance = {self.balance}")

# a1= Account("Shivam12345", "12348765", 3000)
# a1.credit_Amount(2000)
# a1.debit_Amount(6000)
        


# class Shape:
#     def area(self):
#         print("Area of a Shape is nothing")

# class Triangle(Shape):

#     def __init__(self):
#         pass

#     def area(self):
#         print("Area of Triangle")
        
#     def perimeter(self):
#         print("kuch nei")

# t1 = Triangle()
# t1.area()
# t1.perimeter()


# print(2+3) #Maths add
# print("2" + "3") # String Concatenate
# a = [1,2, 3]
# b = [3, 4 , 5]

# print(a+b) #Lists Merge

class Complex:
    def __init__(self, img, real):
        self.img = img
        self.real = real
    
    def get_output(self):
        print(f"{self.img}i + {self.real}")

    def __add__(self, new):
        newImg = self.img + new.img
        newReal = self.real + new.real
        return Complex(newImg, newReal)
        

c1 = Complex(4, 8)
c1.get_output()   

c2 = Complex(3, 7)
c2.get_output()

# c3 = c1.add(c2)
c3 = c1 + c2
c3.get_output()
