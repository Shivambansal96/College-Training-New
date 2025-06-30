




# # Print 1 - 100
# for i in range(100, 0, -1):
#     print(f"Hello{i}")



# num = 2
# for i in range(1, 11):
#     # print(num," x ", i, " = ", num*i )
#     print(f"{num} x {i} = {num*i}")

# i = 1
# while(i <= 100):
#     print(i)
# i+=1
# n = 5
# sum = 0
# for i in range(1, n+1):
#   sum = sum * i

# print(f"Sum of {n} naural Numbers = {sum}")

# # # # # LISTS 
# arr = [10, 20, 80, 40, 50]

# arr.append(60)
# # arr.sort(reverse=True)
# # arr.reverse()

# arr.insert(4, 100)

# arr.remove(80)
# arr.pop(4)
# print(arr)

# moviesInput = input("Enter 3 favourite movie names = ")

# arr = list(map(str, moviesInput.split(",")))
# print(arr)  

# # Palindrome List 
# arr = [1, "abcd", "abcd", 1]

# reversedArr = arr.copy()
# reversedArr.reverse()

# print(reversedArr)

# if(arr == reversedArr):
#     print("Palindrome List")
# else:
#     print("not a Palindrome List")


# # # Target Present in the list
# arr = [3, 4, 53, 45, 1341, 531, 35]

# # # 1st Method
# # target = input()
# target = 53473

# if(target in arr):
#     print("Target is present")
# else:
#     print("Target is NOT present")


# # # 2nd Iterating method
# arr = [3, 4, 53, 45, 1341, 531, 35]

# ## // in-built method || Traversing or iterating on the whole LIST
# for i in arr:
#     print(arr.index(i))

# # using range to traverse
# for i in range(len(arr)):
#     print(i)



# n = (2, 4, 2, 4, 4242, 42, 22, 42)

# print(n.count(4))


# list = []
# tup = ()
# sets = {}


# n = set()
# print(type(n))



# classRooms = {"python", "C++", "java", "js", "MongoDb", "python", "C++", "java", "js", "MongoDb", "python", "C++", "java", "js", "MongoDb"}

# print(len(classRooms))

# # # QUESTION -
# text1 = "Python is a great programming language"
# text2 = "Many developers love the python language"

# textSet1 = set(text1.lower().split())
# textSet2 = set(text2.lower().split())

# # print(textSet1)
# # print(textSet2)

# newSet = textSet1.symmetric_difference(textSet2)


# # # COMMON ELEMENTS
# # # aNb = textSet1 & textSet2
# # aNb = textSet1.intersection(textSet2)
# # print(f" Common words between both Sets = {aNb}")


# # # UNIQUE ELEMENTS IN SET1
# # # aNb = textSet1 - textSet2
# # aNb = textSet1.difference(textSet2)
# # print(f" Unique Elements in Sets 1 = {aNb}")

# # # Count of Unique WOrds
# # aUb = len(textSet1.union(textSet2))
# # aNb = len(textSet1.intersection(textSet2))

# # print(aUb - aNb)

# n = {
#     "name": "Shivam",
#     "marks" : {
#         "python" : 90,
#         "C" : 80,
#         "Web" : 100
#     }
# }

# m = {
#     "age": 24,
#     "price": 10
# }
# n.update(m)

# print(n)


myDict = {}

n = 3

for i in range(n):
    key = input("Enter a key = ")
    value = input("Enter a value = ")

    # myDict[key] = value
    myDict.update({key:value})

print(myDict)

