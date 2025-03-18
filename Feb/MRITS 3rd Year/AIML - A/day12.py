# # # # # # Exception Handling 

# # # # # # a = input("Enter a number = ")
# # # # # # print(f"Multiplication Table of {a} is: ")


# # # # # list = [20, 45]

# # # # # try:
# # # # #     # for i in range(1, 11):
# # # # #         # print(f"{int(a)} x {i} = {int(a)*i}")
# # # # #     print(list[3])

# # # # # except IndexError:
# # # # #     print("Index Out of Bounds !!!")
# # # # #     # print(f"ERROR = {e}")


# # # # # print("CODE ENDS")



# # # # a = 5
# # # # b = 0


# # # # def hello():
# # # #     res = None
# # # #    try:
# # # #      res = (a/b)
        
# # # #    except ZeroDivisionError:
# # # #        # return "The number cannot be divided by 0!"
# # # #        res = "0 not possible"
    
# # # #    finally:
# # # #        print("I will be executed!")

# # # #    return res

# # # # print(hello())



# # # try:

# # #     age = int(input("Enter Age = "))
# # #     if(age < 18 or age > 60):
# # #         if(age < 18):
# # #             print("Person is a Minor")

# # #         else:
# # #             print("Person is a Senior Citizen")

# # #     else:
# # #         raise Exception("Age between 18 to 60.")

# # # except ValueError:
# # #     print("Wrong Input!!!")

# # # Write a Python program that takes two numbers as input and performs division. Use exception handling to manage any potential errors that may occur (e.g., division by zero, invalid input).

# # a = input("Enter num1 = ")
# # b = input("Enter num2 = ")

# # try:
# #     print(int(a)/int(b))

# # except ZeroDivisionError:
# #     print("The second number cannot be a Zero!")

# # except ValueError:
# #     print("Please insert an Integer")


# # Define a custom exception called NegativeNumberError. Write a function check_positive that raises this exception if a negative number is passed to it.

# a = int(input("Enter any number = "))

# if (a < 0):
#     raise Exception("Number is Negative!")

# else:
#     print(a)


# print("CODE ENDS")


# import random
# import math

# a = random.randint(1, 150)

# fact = math.factorial(5)

# print(a)

# print(fact)