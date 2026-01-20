# myArr = [3, 5, 7, 1, 9, 12, 6, 5]

# # myArr.append(1)
# # myArr.sort()
# # myArr.sort(reverse=True)
# # myArr.reverse()
# # myArr.insert(4, 100)
# # myArr.remove(5)
# myArr.pop(5)

# print(myArr)


# movie1 = input("Enter movie 1 = ")
# movie2 = input("Enter movie 2 = ")
# movie3 = input("Enter movie 3 = ")

# myMovies = [movie1, movie2, movie3]

# for i in myMovies:
#     print(i)




# myMovies = [movie1, movie2, movie3]

# myMovies = []

# for i in range(3):
#     movie = input("Enter movie 3 = ")
#     myMovies.append(movie)

# # print(myMovies)
# for i in myMovies:
#     print(i)

# originalList = [1, 2, 4, 6, 4 , 2, 1]
# reversedList = originalList.copy()
# reversedList.reverse()

# if(originalList == reversedList):
#     print("P")
# else:
#     print("NOT P")



# myArr = [3, 42, 42, 13, 40, 4, 31, 42, 9, 9, 24]
# myArr.sort(reverse=True)
# maximumValue = myArr[0]

# for i in myArr:
#     if(i < maximumValue):
#         ans = i
#         break

# print(ans)

# target = 36
# myList = []
# for i in range(1, 11):
#     square = i*i
#     myList.append(square)

# # print(myList)

# for i in range(len(myList)):
#     if(target == myList[i]):
#         print(i)
#         break


# myTuple = (24, 42, 5, 6, 78, 97, 65, 6, 7, 6, 67,65)

# # myTuple[0] = 888

# print(myTuple.count(6))
# # ans = myTuple.count(6)
# ans = myTuple.sort()
# print(ans)


# myTup = ("A", "B", "C", "A", "B", "B", "B", )
# print(myTup.count("B"))

# myList = list(myTup)
# myList.sort()
# print(myList)

# print(myTuple)




# nums = {1, 2, 3, 4, 5, 4, 3, 2, 1} # SET 
# nums = set()

# print(nums)
# print(type(nums))

# nums = {1, 2, 3, 4, 5, 4, 3, 2, 1} # SET 
# nums.add(10)
# nums.remove(4)
# nums.clear()
# nums.pop()

# setA = {1, 2, 3}
# setB = {3, 4, 5}

# ans = setA.union(setB)
# ans2 = setA.intersection(setB)

# print(ans)
# print(ans2)



# classRoom = {"C", "Java", "Js", "MERN", "NODE", "Js", "C", "C++", "C", "Java", "Js"}


# print(len(classRoom))

# firstA = "Python is a great programming language"
# firstB = "Many developers love the python language"

# setA = set(firstA.lower().split(" "))
# setB = set(firstB.lower().split(" "))

# ans = setB.symmetric_difference(setA)

# print(ans)

# aNb = setA.intersection(setB)
# aNb2 = setA & setB
# # print(aNb)
# # print(aNb2)

# diff = setA.difference(setB)
# diff2 = setA - setB
# # print(diff)
# # print(diff2)


# aUb = setA.union(setB)
# aUb2 = setA | setB
# print(aUb)
# print(aUb2)



# mySet = {32, 42, 552, 31, 44, 4, 8}
# myList = list(mySet)
# myList.sort(reverse=True)
# print(myList[1])


# mySet = {32, 42, 552, 31, 44, 4, 8}
# maxValue = max(mySet)
# mySet.remove(maxValue)
# print(max(mySet))