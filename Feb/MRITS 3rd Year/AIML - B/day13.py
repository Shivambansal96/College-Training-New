# # # # # #    ----------------- MAP ----------------

# # # # # # WITHOUT MAP FUNCTION

# # # # # nums = [23, 65, 23, 14, 56, 78]
# # # # # secondNums = []

# # # # # for i in nums:
# # # # #     secondNums.append(i)

# # # # # print(f"Without MAP Function = {secondNums}")

# # # # # # WITH MAP FUNCTION

# # # # # nums = [23, 65, 23, 14, 56, 78]

# # # # # result = list(map(int, nums))
# # # # # print(f"With MAP Function {result}")


# # # # # #    ----------------- FILTER ----------------

# # # # # # WITHOUT FILTER FUNCTION

# # # # nums = [1, 2, 3, 4, 5, 6]
# # # # secondNum = []

# # # # for i in nums:
# # # #     if(i % 2 == 0):
# # # #         secondNum.append(i)
# # # # print(secondNum)


# # # # # # WITH FILTER FUNCTION

# # # # def is_Even(nums):
# # # #     return nums % 2 == 0
# # # # nums = [1, 2, 3, 4, 5, 6]
# # # # result = list(filter(is_Even, nums))
# # # # print(result)

# # # # # #    ----------------- REDUCE ----------------


# # # # # # WITHOUT REDUCE FUNCTION

# # # def addNums(nums):
# # #     sum = 0
# # #     for i in nums:
# # #         sum += i

# # #     return sum

# # # nums = [1, 2, 3, 4, 5]
# # # print(f"Without REDUCE Function = {addNums(nums)}")

# # # # # # WITH REDUCE FUNCTION

# # # from functools import reduce

# # # def addNumInList(accumulatedValue, currentValue):
# # #     return accumulatedValue + currentValue

# # # nums = [1, 2, 3, 4, 5]
# # # result = reduce(addNumInList, nums)
# # # print(f"With REDUCE Function = {result}")




# # # # # #    ----------------- LAMBDA ----------------


# # # # # # WITHOUT LAMBDA FUNCTION

# # def add(a, b):
# #     sum = a+b
# #     return sum

# # print(f"WITHOUT LAMBDA FUNCTION = {add(10, 5)}")


# # # # # # WITHOUT LAMBDA FUNCTION

# # add = lambda a, b : a + b

# # print(f"With LAMBDA Function = {add(10, 5)}")


# # # # GUESS A RANDOM NUMBER GAME

import random

randomNum = random.randint(1, 100)

attempts = 0
diffLevel = input("Enter the difficulty level (Easy, Medium, Hard) = ")

if(diffLevel == "Hard"):
    attempts = 3
    print(f"You have {attempts} attempts left")

elif(diffLevel == "Medium"):
    attempts = 5
    print(f"You have {attempts} attempts left")

else:
    attempts = 10
    print(f"You have {attempts} attempts left")

input("Press Enter to Start the Game.")

while (attempts > 0):
    guessNum = input("Enter an int to play or 'Q' to Quit = ")

    if(guessNum == 'Q'):
        break

    else:
        guessNum = int(guessNum)
        if(guessNum < randomNum):
            print("The actual number is greater")

        elif(guessNum > randomNum):
            print("The actual number is lower")
        
        else:
            print("Congrats You guessed it!")
            break

    attempts -= 1

    if(attempts == 1):
        print("FINAL TRY")


print("----------- GAME OVER -----------")

