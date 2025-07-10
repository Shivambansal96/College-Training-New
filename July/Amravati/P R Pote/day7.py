

# myDict = {
#     "name": "Shivam",
#     "marks": 97
# }

# myDict = {
#     "name": "Shivam",
#     "marks": {
#         "Python" : 99,
#         "Web Dev": 76,
#         "C": 23
#     }
# }


# print(myDict["marks"]["Python"])


# myDict = {
#     "table": ["a piece of furniture", "list of facts and figures"],
#     "cat": "a small animal"
# }
# print(myDict)


# sub1 = input("Enter a subject = ")
# sub2 = input("Enter another subject = ")
# sub3 = input("Enter another subject = ")

# marks1 = int(input(f"Enter marks of {sub1} = "))
# marks2 = int(input(f"Enter marks of {sub2} = "))
# marks3 = int(input(f"Enter marks of {sub3} = "))

# marks = {
#     sub1 : marks1,
#     sub2 : marks2,
#     sub3 : marks3,
# }

# print(marks)

# myDict = {
#     "name": "Shivam",
#     "marks": 99.7,
#     "age" : 24,
#     "isTrainer": True,
#     "Vacation": None
# }

# ans = myDict.keys()
# ans = myDict.values()
# ans = myDict.items()
# print("CODE STARTS")
# ans = myDict.get("Name")
# # print(myDict["Name"])
# print(ans)

# print("CODE ENDS")

# myDict.update({"Chup raho": True})

# print(myDict)





# myDict = {}
# sub1 = input("Enter a subject = ")
# marks1 = int(input(f"Enter marks of {sub1} = "))

# sub2 = input("Enter another subject = ")
# marks2 = int(input(f"Enter marks of {sub2} = "))

# sub3 = input("Enter another subject = ")
# marks3 = int(input(f"Enter marks of {sub3} = "))


# myDict.update({sub1 : marks1})
# myDict.update({sub2 : marks2})
# myDict.update({sub3 : marks3})

# print(myDict)


# myDict = {}

# for i in range(3):
#     sub = input("Enter a subject = ")
#     marks = int(input(f"Enter marks of {sub} = "))

#     myDict.update({sub : marks})

# print(myDict)

# myDict = {}

# for i in range(1, 11):
#     myDict.update({i:i*i})

# print(myDict)


# sent = "python is a great great language is great"

# words = sent.split()
# freqCount = {}

# for i in words:
#     if i in freqCount:
#         freqCount[i] += 1
#     else:
#         freqCount[i] = 1

# print(freqCount)
# ===================================== #

# a = 5
# b = 10

# sum = a + b
# print(sum)

# a = 10
# b = 10

# sum = a + b
# print(sum)

# a = 15
# b = 15

# sum = a + b
# print(sum)

# a = 25
# b = 15

# sum = a + b
# print(sum)

# a = 35
# b = 15

# sum = a + b
# print(sum)


# print("USING FUNCTION")


# def cal_Sum(a, b):
#     sum = a+b
#     print(sum)

# cal_Sum(5, 10)
# cal_Sum(10, 10)
# cal_Sum(15, 15)
# cal_Sum(25, 15)
# cal_Sum(35, 15)


# def cal_Sum(a, c, b= 9):
#     print(a+b+c)

# cal_Sum(8, 5)


myList = [2, 42, 51, 45, 31, 52, 56, 2]

def calculate_length(myList):
    ans = len(myList)
    print(ans)

calculate_length(myList)

