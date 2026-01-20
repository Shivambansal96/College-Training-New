# print("Hello World!","Shivam this side")
# print("Today is day1 of Python")

# first_Name = "Shiv"
# age = 24

# print("My name is", first_Name)
# print("My age is", age)


# a = "5"
# b = 2


# sum = a + b
# print(sum)
# print(type(sum))

# color = input("Enter the colour of the signal = ")

# if(color == "Red"):
#     print(color)
#     print("STOP")              # INDENTATION
# elif(color == "Yellow"):
#     print("REady To Go !!!")
# elif(color == "Green"):
#     print("GO")
# else:
#     print("Invalid Color / Input ")
    

# Grade = int(input("Enter a grade = "))
# if(Grade >= 90):
#     print("Grade A")
# elif(Grade >= 80):
#     print("Grade B")
# elif(Grade >= 70):
#     print("Grade C")
# elif(Grade >= 60):
#     print("Grade D")
# else:
#     print("Grade F")
    


# userName = input("Enter your Username = ")

# if(" " in userName):
#     print("Invalid Username")
# elif(len(userName) < 4):
#     print("Too Short!")
# else:
# #     print("Username Accepted!")

# num1 = int(input("Enter the first Number = "))
# num2 = int(input("Enter the second Number = "))
# num3 = int(input("Enter the third Number = "))

# if(num1 > num2 and num1 > num3):
#     print("Greatest is num1")
# elif(num2 > num1 and num2 > num3):
#     print("Greatest is num2")
# else:
#     print("Greatest is num3")



# num = int(input("Enter a Number = "))

# if num % 7 == 0:
#     print("Multiple of 7")
# else:
#     print("Not a Multiple of 7")


# num = int(input("Enter a Number = "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# for i in range(1, 11):
#     mul = 3*i

#     print("3 x",i, "=", mul)


# for i in range(5):
#     if(i == 3):
#         continue
#     else:
#         print(i)

# i = 0
# while(i < 5):
#     print(i)
#     i+=1



n = int(input("Enter the sum of natural numbers you want = "))

total = 0
for i in range(1, n+1):
    total += i

print(total)