# # # # # # # name = "Shivam"

# # # # # # # # STARTING SUBSTRING
# # # # # # # startingSub = name[0:4]
# # # # # # # startingSub1 = name[:4]

# # # # # # # print(startingSub)
# # # # # # # print(startingSub1)





# # # # # # # # ENDING SUBSTRING
# # # # # # # endingSub = name[4:6]
# # # # # # # endingSub1 = name[4:len(name)]
# # # # # # # endingSub2 = name[4:]

# # # # # # # print(endingSub)
# # # # # # # print(endingSub1)
# # # # # # # print(endingSub2)


# # # # # # name = "Shivam"


# # # # # # # NEGATIVE INDEXING
# # # # # # # STARTS FROM LAST (-1 to -(length of string))
# # # # # # # 3rd index by default is 1 (LEFT TO RIGHT)
# # # # # # # 3rd index -1 (RIGHT TO LEFT)
# # # # # # sub = name[-1:-3:-1]
# # # # # # print(sub)


# # # # # # name = input("Enter your name = ")
# # # # # # print(f"Name = {name}")
# # # # # # print(f"Length of the name = {len(name)}")

# # # # # word = input("Enter a word = ")

# # # # # first_char = word[0]
# # # # # last_char = word[-1] # OR  # last_char = word[len(word)]

# # # # # print(first_char == last_char)


# # # # original_str = input("Enter a word = ")

# # # # # reversed_str = original_str[-1:-len(original_str)-1:-1]

# # # # reversed_str = original_str[::-1]

# # # # print(original_str == reversed_str)


# # # word = "today's topic is Strings in ython"

# # # # ans = word.endswith("in Python")
# # # # ans = word.capitalize()
# # # # ans = word.replace("is Strings", "map, filter, reduce")
# # # # ans = word.find("o")
# # # # ans = word.swapcase()
# # # ans = word.count("p")

# # # print(ans)


# # name = input("Enter your name = ")

# # ans = name.find("a")
# # ans2 = name.count("a")

# # print(f"a is present at index {ans}")
# # print(f"Count of a = {ans2}")


# name = input("Enter your name = ")

# if(name == name.upper()):
#     print("Uppercase")
# elif(name == name.lower()):
#     print("Lowercase")
# else:
#     print("Mixed Case")


# email = input("Enter any email = ")

# # if((email.find("@") != -1) and email.endswith(".com")):
# # if(email.count("@") == 1 and email.endswith(".com")):
# if("@" in email and email.endswith(".com")):
#     print("Valid")
# else:
#     print("Invalid")



age = 190000

# if(age >= 18):
#     if(age >= 60):
#         print("Senior Citizen")
#     else:
#         print("Adult")
# else:
#     print("Minor")


# if(age >= 18 and age <= 60):
#     print("Adult")
# elif(age >= 60):
#     print("Senior Citizen")
# else:
#     print("Minor")


# trafficLight = input("Enter a traffic Light = ")

# if(trafficLight == "red"):
#     print("STOP")
# elif(trafficLight == "green"):
#     print("GO")
# elif(trafficLight == "yellow"):
#     print("Ready to go!!!")
# else:
#     print("Invalid Input")

# marks = 40

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80):
#     grade = "B"
# elif(marks >= 70):
#     grade = "C"
# else:
#     grade = "D"

# print(grade)


# num = int(input("Enter a number = "))

# # Method 1
# if(num % 2 == 0):
#     print("Even")
# else:
    # print("Odd")

# # Method 2
# # if(num % 2 != 0):
# if(num % 2 == 1):
#     print("Odd")
# else:
#     print("Even")


userName = input("Enter a username = ")

if(" " in userName):
    print("Invalid Email")
elif(len(userName) < 4):
    print("Too Short")
else:
    print("Username Accepted!")