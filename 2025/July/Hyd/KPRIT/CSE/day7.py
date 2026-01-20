# myDict = {
#     "name": "Shivam",
#     "age" : 26,
#     "isTrainer" : True,
#     "Check" : None
# }

# # myDict = {"name": "Shiv"}

# myDict["OK"] = "Nothing"

# # myDict["name"] = "Shiv"

# print(myDict)



# myDict = {
#     "name": "Shivam",
#     "age" : 26,
#     "isTrainer" : True,
#     "Check" : None
# }

# print(myDict.items())
# print(myDict)

# print(myDict["nam"])
# print(myDict.get("nam"))

# print("CODE ENDS")


myDict = {
    "name": "Shivam",
    "age" : 26,
    "isTrainer" : True,
    "Check" : None
}

# myDict2 = {
#     "OK": "gurhugb"
# }

# # myDict["OK"] = "nothing"

# # myDict.update({"OK": "NOTHING", "busfrn": "Vuisbviuw"})
# myDict.update(myDict2)

# print(myDict)


# myDict = {
#     "table": ["a piece of furniture", "lists of facts and figures"],
#     "cat" : "A small animal"
# }

# print(myDict)


# myDict = {}

# sub1 = input("Enter the name of Subject 1 = ")
# sub2 = input("Enter the name of Subject 2 = ")
# sub3 = input("Enter the name of Subject 3 = ")

# marks1 = input("Enter the marks of Subject 1 = ")
# marks2 = input("Enter the marks of Subject 2 = ")
# marks3 = input("Enter the marks of Subject 3 = ")

# myDict.update({sub1:marks1})
# myDict.update({sub2:marks2})
# myDict.update({sub3:marks3})

# print(myDict)



# myDict = {}

# for i in range(3):
#     sub = input(f"Enter the name of the Subject {i+1} = ")
#     marks = input(f"Enter the marks of the {sub} = ")

#     myDict.update({sub:marks})

# print(myDict)

# myDict = {}

# for i in range(1, 11):
#     myDict.update({i:i*i})

# print(myDict)



# a = 5
# b = 10
# sum = a + b
# print(sum)

# a = 5
# b = 1076
# sum = a + b
# print(sum)

# a = 52
# b = 10
# sum = a + b
# print(sum)

# a = 531
# b = 10
# sum = a + b
# print(sum)


# def addSum(a, b):
#     s = a + b
#     print(s)
    

# for i in range(3):
#     a = int(input())
#     b = int(input())

#     addSum(a, b)



# def addSum(a, b):
#     s = a + b
#     return s

# a = addSum(9, 9)
# print(a)
# print(addSum(9, 6))

# a = [876, 986]

# len(a)

# a = int(input())
# b = int(input())
# addSum(a, b)

# a = int(input())
# b = int(input())
# addSum(a, b)

# def calc_Length(myList):
#     print(len(myList))

# myList = [42, 53, 53, 63,6 ,63, 4,42, 52]
# calc_Length(myList)

# def eleList(myList):
#     for i in myList:
#         print(i, end=" ")

# myList = [42, 53, 53, 63,6 ,63, 4,42, 52]
# eleList(myList)


# def eleList(myList):
#     for i in range(len(myList)):
#         if(i != len(myList)-1):
#             print(myList[i], end=", ")
#         else:
#             print(myList[i], end=".")

# myList = [42, 53, 53, 63,6 ,63, 4,42, 52]
# eleList(myList)


# def eleList(myList):
#     for i in range(len(myList)):
#         print(myList[i], end=" ")

# myList = [42, 53, 53, 63,6 ,63, 4,42, 52]
# eleList(myList)


def currency_convertor(amount):
    total = amount * 80

    print(f"Rs. {total}")
    # return total

amount = int(input("Enter the amount you want to convert (in $) = "))
currency_convertor(amount)