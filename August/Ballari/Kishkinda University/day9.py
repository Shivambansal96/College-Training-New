# # # BASIC UNDERSTANDING
# myList = [42, 532, 63, 25, 3, 311, 4]
# n = 5
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print("* ", end="")

#     print()

# # # # 1)
# n = int(input("Enter a number = "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end="")
#     # print(f" Row {i} ended")
#     print()


# # # # 1) (i)
# n = int(input("Enter a number = "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     # print(f" Row {i} ended")
#     print()


# # # # 1) (ii)
# n = int(input("Enter a number = "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(i, end=" ")
#     # print(f" Row {i} ended")
#     print()

# # # # 1) (iv)
# n = 5
# for i in range(65, 65+n):
#     for j in range(65, i+1):
#         print(chr(i), end=" ")
#     print()

# # # # 1) (iv)
# n = 5
# for i in range(69, 69-n, -1):
#     for j in range(69, i+1, -1):
#         print(chr(i), end=" ")
#     print()

## E
## D D
## C C C
## B B B B
## A A A A A

# for i in range(69, 64, -1):
#     for j in range(69, i-1, -1):
#         print(chr(i), end=" ")
#     print()

















