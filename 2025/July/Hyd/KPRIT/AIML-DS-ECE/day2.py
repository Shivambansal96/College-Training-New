# # Sum of 2 numbers

# a = int(input("Enter the first number = "))
# b = int(input("Enter the second number = "))

# sum = a + b

# print(f"Sum of {a} and {b} = {sum}")

# # Print the area of a square

# side = int(input("Enter a side = "))

# Area = side * side
# print(f"Area of side {side} is {Area}")


# Print the average of 2 numbers

# num1 = float(input("Enter the first number = "))
# num2 = float(input("Enter the second number = "))

# avg = (num1 + num2) / 2

# print(f"Average = {avg}")

# Chcek if num1 is greater than num2

# a = int(input("Enter the first number = "))
# b = int(input("Enter the second number = "))

# print(a > b)

# # PRint the name and length of the User

# name= input("Enter your name = ")

# print(f"Your name is {name}")
# print(f"Length of your name is {len(name)} characters")

# # Check if 1st and last characters are same or not

# word = input("Enter any word = ").lower()
# print(word)

# print(word[0] == word[-1])


# # # Check if a word is palindrome

# originalWord = input("Enter a word = ")
# # reversedWord = originalWord[-1:-len(originalWord)-1:-1]
# reversedWord = originalWord[::-1]

# print(originalWord == reversedWord)

# color = "guirsohgnwsouhl"
# if(color == "red"):
#     print("STOP")
# elif(color == "green"):
#     print("GO !!!")
# elif(color == "yellow"):
#     print("Ready to go !!")
# else:
#     print("Invalid Input")


# marks = int(input("Enter your marks = "))

# grade = None

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80):
#     grade = "B"
# elif(marks >= 70):
#     grade = "C"
# elif(marks >= 60):
#     grade = "D"
# else:
#     grade = "FAIL"

# if(marks < 90):
#     print("MARKS")

# print(grade)

# UserName Checker

userName = input("Enter an Username = ")

if(" " in userName):
    print("Invalid UserName")
elif(len(userName) < 4):
    print("Username is too Short")
else:
    print("Username Accepted!!")
