
# # # def calculate_Sum(a, b): # def Defining a Function #(parameters: values we pass from the calling  Fn)
# # #     sum = a + b
# # #     print("sum from fn = ", sum)

# # #     return sum          # return: whatever we want to return

# # # result = calculate_Sum(6, 86) # Calling a Function # (arguments: values being passed while calling the Fn)

# # # print(result)




# # nums = [3, 35, 23, 46, 57, 98]
# # numsTwo = [3, 35, 23, 98]

# # def findLength(n):
# #     res = len(n)
    
# #     print(res)

# # findLength(nums)
# # findLength(numsTwo)


# nums = ["Shivam", True, False, 98.73]

# def list_elements(n):
#     for i in n:
#         print(i, end=" ")

# list_elements(nums)


n = int(input("Enter a number = "))
r = int(input("Enter a number = "))

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i

    return fact

numerator = factorial(n)
denominator2 = factorial(r)
denominator = factorial(n-r)

print(numerator // (denominator*denominator2))