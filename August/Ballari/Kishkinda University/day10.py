# # # 1. Reverse a number (Method 1)

# n = int(input("Enter a number = ")) # 123
# stringN = str(n)
# revStr = stringN[::-1]
# revNum = int(revStr)

# print(revNum)
# print(type(revNum))


# # # 1. Reverse a number (Method 2)

# n = 123
# rev = 0

# remainder = n % 10          # 3
# rev = rev*10 + remainder       # 3
# n //= 10

# remainder = n % 10          # 2
# rev = (rev*10) + remainder       # 3*10 + 2 = 30 + 2 = 32
# n //= 10

# remainder = n % 10             # 1
# rev = (rev*10) + remainder      # 32 * 10 + 1 = 320 + 1 = 321
# n //= 10

n = int(input("Enter a number = "))
rev = 0

while(n != 0):
    remainder = n % 10
    rev = (rev*10) + remainder
    n //= 10

print(rev)


