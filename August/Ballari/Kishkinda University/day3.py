

# # n = 5
# # i = 1
# # total = 1
# # while( i <= n):
# #     total = total * i
# #     i += 1
# # print(total)


# # # num1 = int(input("Enter num1 = "))
# # # num2 = int(input("Enter num2 = "))
# # # num3 = int(input("Enter num3 = "))

# # # if(num1 > num2 and num2 > num3):
# # #     print(num1, "is the greatest")
# # # elif(num2 > num3):
# # #     print(num2, "is the greatest")
# # # else:
# # #     print(num3, "is the greatest")



# # newList = ["Shivam", 26, 10_000, True, "Valid"]

# # for i in newList:
# #     print(i)

# # for i in range(1, len(newList), 2):
# #     print(newList[i])

# # newList = ["Shivam", 26, 10_000, True, "Valid"]
# # newList = [32, 42, 7, 13, 42, 1, 2]

# # newList.append(90)
# # newList.sort(reverse=False)
# # newList.sort(reverse=True)
# # newList.reverse()
# # newList.insert(2, "newValue")
# # newList.remove("Valid")
# # newList.pop(3)
# # print(newList.index("Valid"))

# # print(newList)


# # newList = ["Shivam", 26, 10_000, True, "Valid"]
# # newList2 = newList

# # newList.append(24)
# # print(newList2)

# # Method 1
# # mov1 = input("Enter your 1st Fav movie = ")
# # mov2 = input("Enter your 2nd Fav movie = ")
# # mov3 = input("Enter your 3rd Fav movie = ")
# # myMovies = [mov1, mov2, mov3]
# # print(myMovies)

# # # Method 2
# # myMovies = []

# # mov1 = input("Enter your 1st Fav movie = ")
# # mov2 = input("Enter your 2nd Fav movie = ")
# # mov3 = input("Enter your 3rd Fav movie = ")

# # myMovies.append(mov1)
# # myMovies.append(mov2)
# # myMovies.append(mov3)

# # print(myMovies)

# # # Method 3
# # myMovies = []

# # for i in range(1, 4):
# #     movie = input(f"Enter your favourite movie{i} = ")
# #     myMovies.append(movie)

# # print(myMovies)

# # myList = [1, "abc", 5, "abc", 1]
# # revList = myList.copy()
# # revList.reverse()

# # if(myList == revList):
# #     print(f"Palindrome List")
# # else:
# #     print(f"Not a Palindrome List")




# # for i in range(10):
# #     if(i == 5):
# #         break
# #     print(i)

# # else:
# #     print("CODE ENDS")

# # myList = [3333333, 314, 41, 1, 34, 6, 78, 5, 4, 2, 422, 55, 242]

# # target = int(input("Enter a target = "))

# # for i in myList:
# #     if(target == i):
# #         print(f"Target Found at Index {myList.index(i)}")
# #         break
# # else:
# #     print("Target not Found!")



# # myList = [3333333, 314, 41, 1, 34, 6, 78, 5, 4, 2, 422, 55, 242]
# # target = int(input("Enter a target = "))

# # for i in range(len(myList)):
# #     if(target == myList[i]):
# #         print(f"Target Found at Index {i}")
# #         break
# # else:
# #     print("Target not Found!")


# # myList = [3333333, 314, 41, 1, 34, 6, 78, 5, 4, 2, 422, 55, 242]
# # target = 410000
# # if(target in myList):
# #     print("Target Found")
# # else:
# #     print("Target NOT Found")


# # tup = (3,)

# # print(type(tup))
# # print(tup)


# # myList = [("Alice", 31), ("Shivam", 21)]

# # tup = (31, 41, 52, 44, 21, 31, 12)


# # print(tup.count(31))
# # print(tup.index(44))


# # tup = ["C", "A", "D", "B", "A", "C", "D", "A"]
# # print(tup.count("A"))

# # myList = list(tup)
# # myList.sort()
# # print(myList)



# # new = {31, 31, 13, 34, 41, 13}

# # new.add(50)
# # new.remove(31)
# # # new.clear()
# # new.pop()

# # print(new)

# # setA = {1, 2, 3}
# # setB = {3, 4, 5}

# # ans = setA.union(setB)
# # ans = setA.intersection(setB)

# # print(ans)

# # myList = ["python", "java", "C++", "python", "js", "java", "python", "java", "C++", "C"]

# # mySet = set(myList)
# # print(len(mySet))


# text1 = "Python is a great programming language"
# text2 = "Many developers love the python language"
# setA = set(text1.lower().split())
# setB = set(text2.lower().split())

# aUb = setA.union(setB)
# aNb = setA.intersection(setB)
# diff = setA.difference(setB)
# symm_Diff = setA.symmetric_difference(setB)
# print(aNb)





# target=7
# set1=(1,2,3,4,5,6,7,8,9)
# for i in range(0,len(set1)):
#     for j in range(i+1,len(set1)):
#         if(set1[i]+set1[j]==target):
#             print("Target found",set1[i],set1[j])
#             break
# else:
#     print("Not found")
    
    
#     CHEck this code for break 

# target not ffound is till being shown even if the target is found

