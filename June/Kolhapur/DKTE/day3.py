# FUNCTIONS

# a = 50
# b = 10
# sum = a + b
# print(sum)

# a = 30
# b = 20
# sum = a + b
# print(sum)

# a = 20
# b = 30
# sum = a + b
# print(sum)

# 12 Lines 

# def cal_sum(a, b= 5):
#     print(a+b)
#     return

# cal_sum(9)

# # WAF TO PRINT LENGTH OF A LIST
# myList = ["My", "name", "is", "Shivam", "Bansal"]
# myNewList = ["marks", 90, 42, 4252, 452, 262462, 462]

# def list_length(list):
#     print(len(list))

# list_length(myList)
# list_length(myNewList)

# # # WAF TO PRINT THE ELEMENTS OF A LIST
# myList = ["My", "name", "is", "Shivam", "Bansal"]

# def ele_list(list):
#     for i in list:
#         print(i, end=" ")


# ele_list(myList)


# # FACTORIAL OF A NUMBER
# n = int(input("Enter a number = "))

# def factorial(n):
#     fact = 1
    
#     for i in range(1, n+1):
#         fact *= i

#     return fact

# ans = factorial(5)

# print(ans)

# # # # PERMUTATION
# n = int(input("Enter value of N = "))
# r = int(input("Enter value or R = "))

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact

# num = factorial(n)
# denom = factorial(r) * factorial(n - r)
# ans = num // denom

# print(ans)



# def show(n):
#     if(n == 0):
#         return
    
#     print(n)
#     show(n - 1)
#     print(f"Recursive value of {n} ENDS")

# n = 3
# show(n)
# print(f"Recursive value of {n} ENDS IN MAIN")

# # # # FACTORIAL USING RECURSION 
# def factorial(n):
#     if(n == 1):
#         return 1

#     return n * factorial(n - 1)

# n = 5
# ans = factorial(n)
# print(ans)



# # # FILE HANDLING I / O

# # # # Reading a File
# myFile = open("demo.txt") # myFile = open("demo.txt", "r")
# data = myFile.read()
# myFile.close()
# print(data)

# # # # Writing a File (Overwriting)
# myFile = open("demo.txt", "w")
# myFile.write("My name is Shivam Bansal")
# myFile.close()


# # # # Writing a File (Appending)
# myFile = open("demo.txt", "a")
# myFile.write("\nI am a Technical Trainer")
# myFile.close()

# # # # Writing a File (Overwriting)
# myFile = open("practice.txt", "w")
# myFile.write("My name is Shivam Bansal \n I am a Technical Trainer \n I like to teach Web Dev as well.\nShivam")
# myFile.close()

# myFile = open("practice.txt")
# data = myFile.read()
# newData = data.replace("Shivam", "Shiv")
# myFile.close()

# myFile = open("practice.txt", "w")
# myFile.write(newData)
# myFile.close()
