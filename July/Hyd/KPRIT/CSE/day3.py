
# for i in range(5):
#     print("Hello World!!!", i)


# for i in range(1, 5):
#     print("Hello World!!!", i)

# for i in range(1, 5, 2):
#     print("Hello World!!!", i)

# for i in range(1, 101):
#     print(i)

# for i in range(100, 0, -1):
#     if(i == 1):
#         print(i, end=".")
#     else:
#         print(i, end=", ")

# n = int(input("Enter a number = "))
# for i in range(1, 11):
#     mul = n * i
#     # print(f"{n} x {i} = {mul}")
#     print(f"{n} x {i} = {n*i}")


# n = 5
# for i in range(n, n*11, n):
#     print(i)


# n = 1
# while(n <= 5):
#     if(n == 3):
#         continue
#     else:
#         print(n)
#         n+=1


# for i in range(1, 6):
#     if(i == 3):
#         continue
#     print(i)

# sum = 0
# n = 5
# for i in range(1, n+1):
#     sum+=i
#     print(sum)

# n = int(input("Enter a number = "))
# sum = 0
# i = 1
# while(i <= n):
#     sum += i
#     i += 1
# print(sum)


# n = 5
# fact = 1

# for i in range(1, n+1):
#     fact*=i

# print(fact)


# marks = [93, 54, 32, 63, 75, 53]
# marks[0] = 10000
# print(len(marks))

# for i in range(len(marks)):
#     print(marks[i], end=" ")

# for i in marks:
#     print(i, end=" ")

# student = [84, 31, 45, 2]

# student.append(99)
# student.sort()
# student.sort(reverse=True)
# student.reverse()
# student.insert(3, 10_000)
# student.remove(45)
# student.pop(3)
# print(student)


# mov1 = input("Enter 1st Favourite movie = ")
# mov2 = input("Enter 2nd Favourite movie = ")
# mov3 = input("Enter 3rd Favourite movie = ")
# # myList = [mov1, mov2, mov3]
# # print(myList)
# myList = []
# myList.append(mov1)
# myList.append(mov2)
# myList.append(mov3)
# print(myList)

# myList = []
# for i in range(1, 11):
#     myList.append(i*i)

# # print(myList)
# for i in myList:
#     print(i, end=" ")


myList = []
for i in range(1, 11):
    myList.append(i*i)
print(myList)
target = 810
# # METHOD 1
# for i in range(len(myList)):
#     if myList[i] == target:
#         print(i)
#         break

# # METHOD 2

# if target in myList:
#     print(myList.index(target))
#     print("Target Found")
# else:
#     print("Target NOT Found")
