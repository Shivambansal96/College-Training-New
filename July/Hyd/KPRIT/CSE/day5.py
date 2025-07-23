myList = [32, 52, 63, 24, 6,242 , 42]

# for i in range(len(myList)):
#     print(f"{i}", end=":")
#     print(f"{myList[i]}")

# for i in myList:
#     print(i)

# m = [(76, 87), (76, 97), ("86", "87")]



# n = 5
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print("*", end="")
#     print()

# myList = [20, 31, 44, 532, 99]

# # # # 1)
# n = int(input("Enter a num = "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end="")
#     print()


# # # # 2) 
n = int(input("Enter a num = "))
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()
