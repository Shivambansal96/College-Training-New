
# nums = [8, 4, 6, 2, 6, 10]
# target = 8
# myList = []
# nums.sort()

# flag = False # A switch to check whether we found the pairs or not

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         total = nums[i] + nums[j]
#         if( total == target):
#             flag = True
#             # print((nums[i], nums[j]))
#             myList.append((nums[i], nums[j]))
#             break


# if(flag == False):
#     print("Pairs not found")
# else:
#     print(myList)


# nums = [5, 1, 2, 2, 2, 1, 5, 5]
# new_list = []

# for i in range(len(nums)):
#     if nums[i] not in new_list:
#         new_list.append(nums[i])

# print(new_list)



# myDict = {
#     "name": "Shivam",
#     "age": 26,
#     "price": 10000
# }

# myDict2 = {
#     "just CHecking": "OK",
#     "CODE ENDED?": "NOT YET"
# }

# # print(myDict["price"])

# # print(myDict.keys())
# # print(myDict.values())
# # print(myDict)
# # print(myDict.items())
# # print(myDict["nam"])
# # print(myDict.get("nae"))
# # myDict.update({"isTrainer": True, "Are you Okay": "YES"})
# myDict.update(myDict2)

# print(myDict)
# # print("COde ENDS")


# # setA = {1, 2, 3}

# # myDict = {
# #     "name": "Shivam"
# # }

# # print(myDict)
# # print(myDict["name"])

# myDict = {
#     "table": ["a piece of Furniture", "kist of fatcs & figures"],
#     "cat": "A small Animal"
# }

# print(myDict) 


# sub1 = input("Enter 1st Subject = ")
# sub2 = input("Enter 2nd Subject = ")
# sub3 = input("Enter 3rd Subject = ")

# m1 = input("Enter marks of Subject 1 = ")
# m2 = input("Enter marks of Subject 2 = ")
# m3 = input("Enter marks of Subject 3 = ")

# myDict = {
#     sub1:m1,
#     sub2:m2,
#     sub3:m3
# }




# sub1 = input("Enter 1st Subject = ")
# sub2 = input("Enter 2nd Subject = ")
# sub3 = input("Enter 3rd Subject = ")

# m1 = input("Enter marks of Subject 1 = ")
# m2 = input("Enter marks of Subject 2 = ")
# m3 = input("Enter marks of Subject 3 = ")

# myDict = {}

# myDict.update({sub1:m1})
# myDict.update({sub2:m2})
# myDict.update({sub3:m3})

# print(myDict)


# myDict = {}

# for i in range(3):
#     subject = input("Enter the name of the Subject: ")
#     marks = input("Enter the marks of the Subject: ")

#     myDict.update({subject:marks})

# print(myDict)

# myDict = {}
# for i in range(1, 11):
#     myDict.update({i:i*i})

# print(myDict)


# def add_Sum(a, b):
#     sum = a + b
#     print(sum)
#     return 10

# ans = add_Sum(3, 4)   

# print(ans)


# def welcome():
#     print("HELlo wORLD!")

# welcome()
# print()
# len()


# def add_Sum(a, b=6):
#     sum = a + b
#     print(sum)

# ans = add_Sum(3)
# print(ans)



# def length_List(myList):
#     print(len(myList))

# myList = [32, 42, 1, 41, 5, 77, 8, 53, 3, 42]
# length_List(myList)


# def print_elements(myList):
#     for i in range(len(myList)):
#         print(myList[i], end=" ")

# myList = [32, 42, 1, 41, 5, 77, 8, 53, 3, 42]

# print_elements(myList)


# def print_elements(myList):
#     for i in myList:
#         print(i, end=" ")

# myList = [32, 42, 1, 41, 5, 77, 8, 53, 3, 42]
# print_elements(myList)


# def currency_Convertor(amount):
#     total = amount * 80
#     print(f"Rs {total}")

# dollar = int(input("Enter the amount (in $dollars) = $"))
# currency_Convertor(dollar)

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact

# n = int(input("Enter the value of n = "))
# r = int(input("Enter the value of r = "))

# num = factorial(n)
# denom = factorial(n - r) 
# ans = num // denom

# print(ans)


# for i in range(10):
#     print("Hello World")

# def print_method():
#     print("Hello World")


# print_method()
# print_method()
# print_method()

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact

# n = int(input("Enter the value of n = "))
# r = int(input("Enter the value of r = "))

# num = factorial(n)
# denom = factorial(n - r) * factorial(r)
# ans = num // denom

# print(ans)



def num(n):
    if(n == 0):
        return

    print(n)
    num(n-1)
    print(f"CODE ENDS INSIDE THE FUNCTION {n}")

n = 300000000000000000000000
num(n)
print(f"CODE ENDS OUTSIDE THE FUNCTION {n}")




import string

a = string.ascii_letters
a = string.digits
print(a)























