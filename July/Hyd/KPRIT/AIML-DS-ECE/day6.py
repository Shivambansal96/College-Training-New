# myDict = {
#     "name": "Shivam",
#     "isTeacher": True,
#     "marks": 95
# }

# myDict2 = {
#     "age": 26,
#     "gender": "Male"
# }

# myDict.update({"age": 24})
# # print(myDict.get("nam"))
# print(myDict)

# print("CODE ENDS")

# myDict = {
#     "table": ["a piece of furniture", "lists of facts and figures"],
#     "cat": "a small animal"
# }

# myDict["table"][0] = "ok"

# print(myDict)


# myDict = {}
# for i in range(1, 4):
#     sub = input(f"Enter name of Subject {i} = ")
#     marksOfSub  = input(f"Enter marks of {sub} = ")

#     myDict.update({sub: marksOfSub})

# print(myDict)




# myDict = {}

# for i in range(1, 11):
#     myDict.update({i:i*i})

# print(myDict)

# a = 5
# b = 10
# sum = a + b
# print(sum)

# a = 53
# b = 120
# sum = a + b
# print(sum)

# a = 53
# b = 130
# sum = a + b
# print(sum)

# a = 15
# b = 30
# sum = a + b
# print(sum)

# def calSum (a, b= 2):
#     sum = a + b
#     print(sum)


# print(calSum(6, 3))




# def lisLength(a):
#     print(len(a))

# myList = [42, 53, 5364, 64, 64, 7, 4 ,32]
# lisLength(myList)


# def printList(list):
#     for i in list:
#         print(i, end=", ")

# myList = [42, 53, 5364, 64, 64, 7, 4 ,32]
# printList(myList)

# def currencyConvertor(n):
#     amount = n * 80

#     return amount

# n = int(input("Enter the Amount you want to convert(in $) = "))

# print(f"Rs. {currencyConvertor(n)}")


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i

    return fact

n = 5
r = 2
print(factorial(n)//factorial(n-r))


