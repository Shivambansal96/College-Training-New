# # # Q1. Reverse a Number

# # Method 1 

# originalNumber = 961
# strNumber = str(originalNumber) # Convert int to String

# result = int(strNumber[::-1])

# print(result)
# print(type(result))

# # METHOD 2

# originalNum = 962
# reversedNum = 0

# while(originalNum != 0):

#     remainder = originalNum % 10
#     reversedNum = reversedNum * 10 + remainder
#     originalNum //= 10

# print(reversedNum)


# # # Q10. Python Mutations

# inputStr = input("Enter a String = ")

# idx = int(input("Enter the index = "))
# valueToChange = input("Enter the character you want to change = ")

# result = inputStr[:idx] + valueToChange + inputStr[idx+1:]

# print(result)

# # # Q3. Two Sum

# numList = list(map(int, input("Enter the list of numbers = ").split()))
# target = int(input("Enter a target = "))

# numList = [2, 7, 11, 15]
# target = 9
# flag = False

# for i in range(len(numList)):
#     for j in range(i+1, len(numList)):
#         if(numList[i] + numList[j] == target):
#             flag = True
#             break

#         else:
#             flag = False

#     if(j != len(numList)):
#         break


# if(flag):
#     print(f"Elements found at index = {[i, j]}")
#     print(f"Elements = {[numList[i], numList[j]]}")
# else:        
#     print(-1)

# # #USING BINARY SEARCH

# numList = [12, 2, 17, 11, 7, 77]
# target = 9

# numList.sort()

# start = 0
# end = len(numList) - 1

# while(start <= end):
#     sum = numList[start] + numList[end]
#     if(sum == target):
#         print(numList[start], numList[end])
#         break

#     elif(sum < target):
#         start = start + 1

#     else:
#         end = end - 1


# numList = [12, 2, 17, 11, 7, 77]
# target = 9
# result = {}
# for i in range(len(numList)):
#     diff = target - numList[i]

#     if(diff in result):
#         print(result[diff], i)
#         break

#     result[numList[i]] = i


# a = "silent"
# b = "listen"

# listA = list(a)
# listB = list(b)

# listA.sort()
# listB.sort()

# print(listA == listB)

# ----------------------- #

# n = int(input("Enter the number of Students = "))
# nameList = []
# scoreList = []
# for i in range(n):
#     name = input("Enter name = ")
#     score = float(input("Enter score = "))

#     nameList.append(name)
#     scoreList.append(score)

# myList = list(set(scoreList))
# myList.sort()
# secondLowest = (myList[1])

# name = []
# for i in range(len(scoreList)):
#     if(scoreList[i] == secondLowest):
#         name.append(nameList[i])

# name.sort()

# print(name)




# num = 201
# duplicateNum = str(num)
# reverseNum = int(duplicateNum[::-1])

# if(num == reverseNum):
#     print("Plaindrome Number")
# else:
#     print("Not a Plaindrome Number")

# num = 112
# originalNum = num
# reversedNum = 0

# while num != 0:
#     remainder = num % 10
#     reversedNum = reversedNum * 10 + remainder
#     num //= 10

# print(originalNum == reversedNum)



# s1 = "silent"
# s2 = "listen"

s1 = "hello"
s2 = "bello"

if(len(s1) == len(s2)):
    count = 0
    for i in range(len(s1)):
        if(s1[i] in s2):
            count += 1
        
    if(count == len(s1)):
        print(f"{s1} and {s2} ARE anagrams")
    else:
        print(f"{s1} and {s2} are NOT anagrams")
else:
    print(f"{s1} and {s2} are NOT anagrams")

# list1 = list(s1)
# list2 = list(s2)

# list1.sort()
# list2.sort()

# print(list1)
# print(list2)

# print(list1 == list2)