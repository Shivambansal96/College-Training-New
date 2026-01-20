
# def calculate_Sum(a, b): # def = defining a Fn # Parameters = values used from the calling Fn/ values used hwile defining the Fn
#     sum = a + b
#     print("inside the Fn= ", sum)
#     return 20

# result = calculate_Sum(5, 10)
# print(result)


# def avgFn(a = 76, b = 7, c = 98):
#     average = (a + b + c) / 3
#     return average


# res = avgFn(67)
# print(res)


# print("Hello World", end=",") # the seperator between 2 outputs in 1 print statement is a space by default


# nums = [12, 34, 13, 134, 14]
# nums2 = [12, 34, 14]

# def lengthOfList(nums):
#     return len(nums)

# result = lengthOfList(nums)
# print(result)

# result2 = lengthOfList(nums2)
# print(result2)



# nums = [12, 34, 13, 134, 14]

# def printList(nums):
#     for i in nums:
#         print(i, end=" ")

# printList(nums)

n = int(input("Enter num = "))
r = int(input("Enter num = "))

def factorial(n):

    fact = 1

    for i in range(1, n+1):
        fact = fact * i

    return fact
print(factorial(n)/factorial(n-r))