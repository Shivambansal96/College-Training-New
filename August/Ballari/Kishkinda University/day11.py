

# n = 5
# new = 5
# for rows in range(1, n+1):
#     for cols in range(1, n - rows + 2):
#         print(rows, end=" ")
#         new -= 1

#     new = n - rows
#     print()

# ------------------------------------ #

# n = 5
# for rows in range(n):
#     for cols in range(n-rows, 0, -1):
#         print(rows, end=" ")

#     print()

# ------------------------------------ #

# n = 5
# for rows in range(1, n+1):
#     for cols in range(n-rows+1, 0, -1):
#         print(cols, end=" ")

#     print()

# ------------------------------------ #

# n = 5
# for rows in range(n, 0, -1):
#     for cols in range(1 , rows+1):
#         print(rows, end=" ")

#     print()

# ------------------------------------ #

# n = 5
# for rows in range(1, n+1):
#     for spaces in range(rows, n):
#         print(" ", end=" ")

#     for stars in range(1, rows+1):
#         print("*", end=" ")

#     print()

# ------------------------------------ #

# n = 5
# for rows in range(n):
#     for spaces in range(rows, n-1):
#         print(" ", end="")

#     for stars in range(rows+1):
#         print("* ", end="")

#     print()

# ------------------------------------ #

# n = 5
# for rows in range(n):
#     for spaces in range(rows, n):
#         print(" ", end="")

#     for stars in range(rows+1):
#         print(rows+1, end="")

#     print()

# ------------------------------------ #

# n = 5
# for rows in range(n):
#     for spaces in range(rows, n):
#         print(" ", end="")

#     for stars in range(rows+1):
#         print(stars+1, end="")

#     print()

# ------------------------------------ #

# n = 5
# for rows in range(1, n+1):
#     for spaces in range(rows, n):
#         print(" ", end="")

#     for stars in range(1, rows+1):
#         print("*", end=" ")

#     print()

# ------------------------------------ #

# n = 5
# for rows in range(1, n+1):
#     for spaces in range(1, rows):
#         print(" ", end="")
        
#     for stars in range(n, rows-1, -1):
#         print("*", end="")

#     print()

# ------------------------------------ #

# n = 5
# for rows in range(1, n+1):
#     for spaces in range(1, rows):
#         print(" ", end="")
        
#     for stars in range(0, n - rows + 1):
#         print(stars + 1, end="")

#     print()


# ------------------------------------ #

# n = 5
# for rows in range(1, n+1):
#     for spaces in range(1, rows):
#         print(" ", end="")
        
#     for stars in range(0, n - rows + 1):
#         print(rows, end="")

#     print()



# ------------------------------------ #

# n = 5
# for rows in range(n):
#     for cols in range(n):
#         if(rows == 0 or rows == n-1 or cols == 0 or cols == n - 1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")

#     print()


# ------------------------------------ #

# n = 5
# for rows in range(n):
#     for cols in range(n):
#         if(rows == n//2 or rows == 0 or rows == n-1 or cols == 0 or cols == n - 1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")

#     print()


# n = 5
# for rows in range(n):
#     for cols in range(n):
#         if(rows == cols or rows == n-cols-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")

#     print()


# n = 5
# for rows in range(1, n+1):
#     for cols in range(1, n+1):
#         if(rows == cols or rows == n-cols+1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")

#     print()


# # # # DIAMOND

# n = 5
# for rows in range(1, n):
#     for spaces in range(rows, n):
#         print(" ", end="")

#     for stars in range(1, rows+1):
#         print("*", end=" ")

#     print()

# n = 5
# for rows in range(1, n+1):
#     for spaces in range(1, rows):
#         print(" ", end="")

#     for stars in range(rows, n+1):
#         print("*", end=" ")

#     print()




# # # # HourGlass

# n = 5
# for rows in range(1, n):
#     for spaces in range(1, rows):
#         print(" ", end="")

#     for stars in range(rows, n+1):
#         print("*", end=" ")

#     print()



# n = 5
# for rows in range(1, n+1):
#     for spaces in range(rows, n):
#         print(" ", end="")

#     for stars in range(1, rows+1):
#         print("*", end=" ")

#     print()




# # # # HourGlass

# n = 5
# for rows in range(1, n):
#     for spaces in range(1, rows):
#         print("*", end=" ")

#     for stars in range(rows, n+1):
#         print(" ", end="")

#     print()



# n = 5
# for rows in range(1, n+1):
#     for spaces in range(rows, n):
#         print("*", end=" ")

#     for stars in range(1, rows+1):
#         print(" ", end="")

#     print()





# # # # # HACKERRANK # # # # # 



# # # NESTED LISTS


# if __name__ == '__main__':
    
#     studentList = []
#     scoreList = set()
    
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
        
#         scoreList.add(score)
#         studentList.append((name, score))

#     scoreList = list(scoreList)
#     scoreList.sort()
#     secondLowest = scoreList[1]
    
#     newList = []
    
#     for i in range(len(studentList)):
#         if(studentList[i][1] == secondLowest):
#             newList.append(studentList[i][0])

#     newList.sort()
        
#     for i in newList:
#         print(i)




