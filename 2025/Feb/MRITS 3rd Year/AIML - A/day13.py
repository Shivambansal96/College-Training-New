
# # # # # ------------------- MAP -----------------------------

# # # # # # Without Map function
# # # # # nums = [32, 33, 13, 93, 12]

# # # # # secondNums = []

# # # # # for i in nums:
# # # # #     secondNums.append(i)

# # # # # print(f"Second List = {secondNums}")


# # # # # # MAP FUNCTION
# # # # # nums = [32, 33, 13, 93, 12, 32, 93]

# # # # # res = set(map(int, nums))

# # # # # print(res)

# # # # # ------------------- FILTER -----------------------------

# # # # # # Without Filter Function

# # # # nums = [32, 33, 13, 93, 12, 93]
# # # # secondNums = []

# # # # for i in nums:
# # # #     if(i % 2 == 0):
# # # #         secondNums.append(i)
# # # # print(secondNums)

# # # # # # Filter Function

# # # # def isEven(nums):
# # # #     return nums % 2 == 0

# # # # nums = [32, 33, 13, 93, 12, 93]
# # # # evenNumber = filter(isEven, nums)
# # # # print(list(evenNumber))


# # # # # # ------------------- REDUCE -----------------------------

# # # # # # # Without Reduce Function

# # # nums = [1, 2, 3, 4, 5]
# # # sum = 0
# # # for i in nums:
# # #     sum += i

# # # print(sum)

# # # # # #  Reduce Function

# # # from functools import reduce

# # # def add(accumulatedValue, currentValue):
# # #     return accumulatedValue + currentValue

# # # nums = [1, 2, 3, 4, 5]
# # # sumOfList = reduce(add, nums)
# # # print(sumOfList)


# # # # # # ------------------- LAMBDA -----------------------------

# # # # # # # Without Lambda Function Example 1

# # def add(a, b):
# #     return a + b

# # print(add(3, 5))

# # # # # # # Lambda Function Example 1

# # add = lambda a,b: a+b
# # print(add(30 , 50))


# # # # # # Without Lambda Function Example 2

# # def mx(a, b):
# #     if(a > b):
# #         return a
# #     else:
# #         return b
# # print(mx(10, 5))

# # # # # # # Lambda Function Example 2

# # mx = lambda a, b: a if a > b else b
# # print(mx(10, 5))




# # # # # # GUESS A RANDOM NUMBER

import random

randomNum = random.randint(1, 100)
guessNum = 0
attempts = 0

diffLevel = input("Enter a difficulty level(Easy, Medium, Hard) = ")

if(diffLevel == "Hard"):
    attempts = 3
    print(f"You have {attempts} Chances to guess the Correct Number")

elif(diffLevel == "Medium"):
    attempts = 5
    print(f"You have {attempts} Chances to guess the Correct Number")

elif(diffLevel == "Easy"):
    attempts = 10
    print(f"You have {attempts} Chances to guess the Correct Number")

else:
    print("Invalid Input!")

while (attempts > 0):
    guessNum = input("If you want to play Enter a number or Enter 'Q' to Quit = ")

    if(guessNum == 'Q'):
        break

    else:
        guessNum = int(guessNum)
        if(guessNum > randomNum):
            print("Your guess is higher than the actual number")
        elif(guessNum < randomNum):
            print("Your guess is lower than the actual number")
        else:
            print("SUCCESS - You guessed it Correct!")

    attempts -= 1

    if(attempts == 1):
        print("LAST TRY!")



print("---------- GAME OVER ---------------")