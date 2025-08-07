
# def print_Elements(i, n):
#     if(i == n+1):
#         return

#     print(i)
#     print_Elements(i+1, n)

# i = int(input("Enter the number you want to start from = "))
# n = int(input("Enter the number you want to end at = "))
# print_Elements(i, n)

# def natural_nums_sum(n):
#     if(n == 1):
#         return 1

#     return n * natural_nums_sum(n - 1)

# n = int(input("Enter a number = "))
# ans = natural_nums_sum(n)
# print(ans)


# def factorial(n):
#     if(n == 1):
#         return 1

#     return n * factorial(n - 1)

# n = int(input("Enter a number = "))
# ans = factorial(n)
# print(ans)


# def permutation(n, r):
#     def factorial(n):
#         if(n == 1):
#             return 1

#         return n * factorial(n - 1)

#     num = factorial(n)
#     denom = factorial(n - r)
#     perm = num // denom
#     return perm

# def combination(n, r):
#     def factorial(n):
#         if(n == 1):
#             return 1

#         return n * factorial(n - 1)

#     num = factorial(n)
#     denom = factorial(n - r)* factorial(r)
#     com = num // denom
#     return com


# n = int(input("Enter n value = "))
# r = int(input("Enter r value = "))
# perm = permutation(n, r)
# print(f"Permutation = {perm}")

# com = combination(n, r)
# print(f"Combination = {com}")

# def print_List(myList, i):
#     if(i == len(myList)):
#         return

#     print(myList[i], end=" ")
#     return print_List(myList, i + 1)

# i = 0
# myList = [31, 31, 41, 4, 145, 78, 6]
# print_List(myList, i)


# total = lambda a, b: a+b
# print(total(3, 5))

# ans = lambda a, b: a if a > b else b
# print(ans(40, 10))

# myList = [43, 42, 1, 34, 4]

# list(map(lambda i: print(myList[i], end=" "), range(len(myList))))

# squareOFANumber = lambda x:x*x
# x = int(input("Enter a number = "))
# print(squareOFANumber(x))


# n = int(input("Enter the size of the list = "))
# myList = []
# for i in range(n):
#     newValue = int(input("Enter a value = "))
#     myList.append(newValue)

# print(myList)

# a = list(map(int, input("Enter the values of the list separated by a space = ").split()))
# print(a)

# a = list(map(int, input("Enter the values of the list separated by a comma = ").split(",")))
# print(a)


# a = list(map(int, input().split()))
# print(a)

# # PRINT ELEMENTS OF A LIST USING LAMBDA FUNCTION
# #PRINT THE INDEX VALUES AND THEN THE VALUES

# myList = [32, 42, 5, 7, 8, 52, 31]

# list(map(lambda i: print(f"Index = {i}, Value = {myList[i]}"), range(len(myList))))

# num = [1, 2, 3, 4, 5]
# ans = lambda i:i * 2
# print(ans(num))


# print(int(input()))
# print("CODE ENDS")

# try:
#     n = int(input())
#     print(n)

# except ValueError:
#     print("WRONG Code")

# except KeyError:
#     print(f"Error = Please dont be an idiot and enter a number")


# # except Exception as e:
# #     print(f"Error = {e}")
# #     print(f"Error = Please dont be an idiot and enter a number")



# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# try:
#     ans = num1 // num2
#     print(ans)

# except ZeroDivisionError:
#     print(f"The Second number cannot be Zero.")

# finally:
#     print("CODE ENDS")


# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))

#     div = num1 // num2
#     print(div)

# except ValueError:
#     print("Enter numbers only.")

# except ZeroDivisionError:
#     print(f"The Second number must be 0.")

# finally:
#     print("Execution Completed.")



# age = 10
# if(age < 18 or age > 60):
#     raise ValueError("Age is wrong!!!")



# name = input("Enter your name = ")

# if(name == ""):
#     raise ValueError("Name cannot be EMpty.")
# else:
#     print(name)

# newFile = open("sample.txt", "r")
# data = newFile.readline()
# newFile.close()

# print(data)

# newFile = open("demo.txt", "w")
# newFile.write("Shivam Bansal")

# newFile = open("demo.txt", "a")
# newFile.write("\nOK NEW Data inserted.")

# newFile = open("demo.txt")
# data = newFile.read()
# print(data)

# import os

# os.remove("demo.txt")
# os.rename("sample.txt", "demo.txt")


newFile = open("practice.txt", "w")
newFile.write("Hi everyone.\nWe are learning File Handling I/O\nusing python\nI like programming in Python.")
newFile.close()

newFile = open("practice.txt", "r")
data = newFile.read()
newFile.close()
print(data)

newData = data.lower().replace("python", "JavaScript")
newFile = open("practice.txt", "w")
newFile.write(newData)

