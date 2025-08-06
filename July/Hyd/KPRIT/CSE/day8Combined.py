

# # # def fact(n):
# # #     factorial = 1
# # #     for i in range(1, n+1):
# # #         factorial *= i

# # #     return factorial
    
# # # # factorial = fact(5)

# # # n = 5
# # # r = 2
# # # num = fact(n)
# # # denom = fact(n - r)
# # # perm = num // denom
# # # print(f"Permutation of {n} and {r} = {perm}")

# # # denom = fact(n-r) * fact(r)
# # # combination = num // denom

# # # print(f"Combination of {n} and {r} = {combination}")


# # def show(n):
# #     # if(n == 0):
# #     #     return
    
# #     print(n)
# #     show(n-1)
# #     print(f"CODE ENDS INSIDE FUNCTION {n}")

# # n = 5
# # show(n)
# # print(f"CODE ENDS OUTSIDE FUNCTION {n}")




# # n = 5
# # sum = 0
# # for i in range(1, 6):
# #     sum+= i

# # print(sum)

# # def natural_nums_Sum(n):
# #     if(n == 1):
# #         return 1
# #     else:
# #         return n + natural_nums_Sum(n - 1)

# # n = 5
# # result = natural_nums_Sum(n)
# # print(result)




# # def factorial(n):
# #     if(n == 1):
# #         return 1
# #     else:
# #         return n * factorial(n - 1)

# # n = 5
# # result = factorial(n)
# # print(result)




# # fileName = open("demo.txt")
# # data = fileName.readline()
# # print(data)

# # fileName = open("demo.txt", "w")
# # fileName.write("Delete Other THings!!")
# # fileName.close()

# # # fileName = open("demo.txt", "a")
# # # fileName.write("\nNew things added!!")
# # # fileName.close()


# # fileName = open("demo.txt", "r")
# # data = fileName.read()
# # fileName.close()
# # print(data)

# # import os

# # # os.remove("demo.txt")
# # os.rename("demo.txt", "test.txt")


# # fileName = open("practice.txt", "w")
# # fileName.write("Hi everyone\nWe are learning file handling I/O\nusing python.\nI like programming in Python.")

# # fileName = open("practice.txt", "r")
# # data = fileName.read()
# # data = data.lower()
# # print(data.find("learning"))
# # newData = data.replace("python", "javaScript")

# # fileName = open("practice.txt", "w")
# # fileName.write(newData)



# # def addSum(a, b):
# #     sum = a+ b
# #     return sum

# # print(addSum(3, 4))

# # addSUM = lambda x,y: x + y
# # print(addSUM(4, 3))

# # sq = lambda x:x**2

# # print(sq(5))

# # myList = [1, 2, 3, 4, 5]
# # pr = list(map(lambda x:x*2, myList))
# # print(pr)

# # listInp = set(map(int, input().split()))
# # print(listInp)


# # print(5/0)  



# # try:
# #     a = int(input("Enter a number = "))

# #     for i in range(1, 11):
# #         print(a)

# # except Exception as e:
# #     print(f"Invalid Input = {a}")
# #     print(f"Error = {e}")


# try:
#     a = int(input())
#     print(a)
    
# except:
#     raise ValueError("Value cannot be a String")


# # except ValueError:
# #     print(f"Value cannot be a String")

# # finally:
# #     print("CODE ENDS")

import string
import random

# allCharacters = string.printable
allCharacters = string.ascii_letters + string.digits + "@!$#%&()"

n = int(input("Enter the length of your random Password = "))
# n = 5

randomPass = ""
for i in range(n):
    randomChoice = random.choice(allCharacters)
    randomPass += randomChoice

print(randomPass)
