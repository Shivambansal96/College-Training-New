# # 1) Sum of 2 numbers

# a = int(input("Enter a number = "))
# b = int(input("Enter another number = "))
# sum = a + b

# print(f"Sum of {a} and {b} = {sum}")

# # 2) Input a side and Print its area

# side = int(input("Enter a side = "))
# Area = side*side
# print(f"Area of {side} = {Area}")


# # 3) Input 2 floating numbers and print their average

# num1 = float(input("Enter First number = "))
# num2 = float(input("Enter Second number = "))

# Average = (num1 + num2) / 2
# print(f"Average of {num1} and {num2} = {Average}")

# # 4) Take input of 2 numbers and print the greatest.

# num1 = int(input("Enter the First number = "))
# num2 = int(input("Enter the Second number = "))

# print(num1 >= num2)

# # 5) 
# i) Take input of a name, print it and its length
# ii) Check the count and occurance of any Alphabet.

# name = input("Enter your name = ")
# inputOfAlphabet = input("The alphabet you want to count = ")
# countOfAlphabet = name.count(inputOfAlphabet)
# FirstOccuranceOfInput = name.find(inputOfAlphabet)
# print(f"Your name is {name}")
# print(f"The Length of your name is {len(name)} characters")   
# print(f"{inputOfAlphabet} appears {countOfAlphabet} time(s)")
# print(f"{inputOfAlphabet} is at index {FirstOccuranceOfInput}")


# # 6) Check whether the 1st and Last character is Same

# a = input("Enter a word = ").lower()

# print(a[0] == a[-1])


# # 7) Check if a word is Palindrome

# originalWord = input("Enter a word = ")

# # reversedWord = originalWord[-1:-len(originalWord)-1:-1]
# reversedWord = originalWord[::-1]

# print(originalWord == reversedWord)

# age = 200

# if(age < 18):
#     print("USer is a KID")
# else:
#     if(age < 60):
#         print("USer can Vote")
#     else:
#         if(age < 100):
#             print("USer can OLD")
#         else:
#             print("USer is DEAD")


# signal = input("Enter the traffic light = ")

# if(signal == "red"):
#     print("STOP")
# elif(signal == "yellow"):
#     print("READY TO GO !!!")
# elif(signal == "green"):
#     print("GO !!!")
# else:
#     print("Invalid Input")


# marks = int(input("Enter marks of the student = "))

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
#     grade = "F"

# if(marks < 80):
#     print("Marks")

# print(grade)

# # 8) Check if a number is Even or Odd

# num = int(input("Enter a number = "))

# if(num % 2 == 0):
#     print(f"{num} is Even")
# else:
#     print(f"{num} is Odd")

# # 9) Valid UserName Checker

# # METHOD 1
# userName = input("Enter a Username = ")

# if(" " in userName):
#     print("Invalid Username")
# elif(len(userName) < 4):
#     print("Too Short")
# else:
#     print("Username accepted.")

# # METHOD 2
# userName = input("Enter a Username = ")

# if(" " not in userName):
#     if(len(userName) >= 4):
#         print("Username accepted.")    
#     else:
#         print("Too Short")
# else:
#     print("Invalid Username")

# # 10) Maximum of 3 numbers

# num1 = int(input("Enter First Number = ")) # 2
# num2 = int(input("Enter Second Number = ")) # 14
# num3 = int(input("Enter Third Number = ")) # 4

# # if(num1 > num2 and num1 > num3):
# #     print(f"{num1} is the Greatest.")
# # elif(num2 > num3):
# #     print(f"{num2} is the Greatest.")
# # else:
# #     print(f"{num3} is the Greatest.")
    

# print(min(num1, num2, num3))