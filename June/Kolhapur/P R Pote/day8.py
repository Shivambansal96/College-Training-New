
# def factorial(n):
#     mul =1
#     for i in range(1, n+1):
#         mul *= i
#     # print(mul)
#     return mul
# n = 5
# r = 5
# factOfN = factorial(n)
# factOfN_R = factorial(n-r)
# permutation = factOfN / factOfN_R

# print(permutation)

# def factorial(n):
#     mul =1
#     for i in range(1, n+1):
#         mul *= i
#     # print(mul)
#     return mul
# n = 5
# r = 5
# factOfN = factorial(n)
# factOfN_R = factorial(n-r)
# permutation = factOfN / factorial(r) * factOfN_R

# print(combination)


# # RECURSION

# def show(n):
#     if(n == 0):
#         return
#     # print(f"Before Function ends at value {n}")
#     show(n-1)
#     # print(f"After Function ends at value {n}")

# print("CODE STARTS")
# n = 10
# r = 43
# show(n)


# print("CODE ENDS")




# def add_sum(n):
#     if(n == 0):
#         return 0

#     return n + add_sum(n-1)

# n = 5
# ans = add_sum(n)
# print(ans)



# def factorial(n):
#     if(n == 0):
#         return 1

#     return n * factorial(n-1)

# n = 5, r = 5
# numerator = factorial(n)
# denominator = factorial(n-r)

# permutation = numerator / denominator




# def factorial(n):
#     if(n == 0):
#         return 1

#     return n * factorial(n-1)

# n = 5, r = 5
# numerator = factorial(n)
# denominator = factorial(n-r) * factorial(r)

# permutation = numerator / denominator


# # FILE I/O

# myFile = open("demo.txt")
# data = myFile.readline()
# myFile.close()

# myFile = open("demo.txt", "a")
# ans = myFile.write("\nHi my name is Shivam TOday we are going to learn Python")
# myFile.close()
# print(ans)

# myFile = open("demo.txt")
# data = myFile.read()
# print(data)

# myFile = open("practiceTest1.txt", "w")
# myFile.write("Hi everyone. \nWe are learning File Handling I/O \nusing Python \nI like programming in python.")
# myFile.close()

# myFile = open("practiceTest1.txt", "r")
# data = myFile.read()
# newData = data.replace("Python", "python")
# newData2 = newData.replace("python", "JavaScript")
# myFile.close()

# myFile = open("practiceTest1.txt", "w")
# myFile.write(newData2)
# myFile.close()


