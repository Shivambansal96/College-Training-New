# # # # # # Exception Handling
# # # # # def hello():
# # # # #     try:

# # # # #         a = 5
# # # # #         b = 0
# # # # #         c = "str"

# # # # #         div = int(a)/int(b)
# # # # #         check = int(a)/int(c)

# # # # #         # print(div)
# # # # #         return div

# # # # #     except ValueError:
# # # # #         return "Invalid Input!"

# # # # #     except ZeroDivisionError:
# # # # #         return "Number cannot be divided by 0"

# # # # #     finally:
# # # # #         print("CODE ENDS inside Finally block")


# # # # # print(hello())

# # # # # print("CODE ENDS in Global Scope")




# # # # age = 47

# # # # if(age < 18 or age > 60):
# # # #     if(age < 18):
# # # #         print("Minor")
# # # #     else:
# # # #         print("Senior Citizen")

# # # # else:
# # # #     raise Exception("Age is not according to the requirements.")

# # # # print("CODE ENDS")

# # # Write a Python program that takes two numbers as input and performs division. Use exception handling to manage any potential errors that may occur (e.g., division by zero, invalid input).

# # # num1 = input("Enter num1 = ")
# # # num2 = input("Enter num2 = ")

# # # try:
# # #     print(int(num1)/int(num2))

# # # except ZeroDivisionError:
# # #     print("Number has been divided by 0!!!")

# # # except ValueError:
# # #     print("Invalid Input Type. Please enter integers!")


# # # Define a custom exception called NegativeNumberError. Write a function check_positive that raises this exception if a negative number is passed to it.
# # try:

# #     a = int(input("Enter Number = "))
# #     if(int(a) < 0):
# #         raise Exception("Number is Negative")
# #     else:
# #         print(a)

# # except ValueError:
# #     print("Enter an Integer")

# # Random and Math Libraries
# import random
# import math

# fact = math.factorial(10)

# print(fact)

# num = random.randint(1, 100)

# print(num)