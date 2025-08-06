# # # # print("Hello wOrld!")
# # # # print("Shivam Bansal", "OK SAME Line", sep="-")
# # # # print("I will be teaching python today.")


# # # print("Hello", end=" - ")
# # # print("World", end=" |")
# # # print("Again")



# # name1 = "Shivam"
# # # 1name = "ufgw"


# # print(3+4)

# a = 45
# b = 10
# sum = a + b
# print(sum)
# a = sum(2, 4)
# print(sum(3, 5))

# a = 45
# b = 10
# mul = a * b
# print(mul)

# print(5/2)
# print(5//2) # floor Division   


# a = 5

# # a = a + 5
# a -= 5

# print(a)



# print((2 == 2 and 5 == 5) or 62 == 6)


# a = 6
# b = "2"
# c = int(b) # Type Casting (Manual Conversion)

# total = a + c

# print(type(b))
# print(b)
# print()
# print(type(c))
# print(c)
# print(total)

# a = int(input("Enter your age = "))

# print(a)
# print(type(a))

# a = "Hello"
# b = 3
# print(a * b)


# name = input("Enter your name = ")
# age = input("Enter your age = ")
# city = input("Enter your city = ")

# print("Hello", name, "you are", age, "years old and live in", city)

# print(f"Hello {name}, you are {age} years old and live in {city}.")


# a = 4
# b = 2

# print(a >= b)

# a = "Shivam"
# b = "Bansal"

# # print(len(a))

# # print(a + " " + b)

# a[0] = "B"  # IMMUTABLE



a = "Shivam"
# ans = a[0:4]
# ans = a[:4]

# ans = a[4:6]
# ans = a[4:len(a)]
# ans = a[4:]

# ans = a[4:0:-1]
# ans = a[5:1:-1]
# ans = a[4:1:-1]

# ans = a[0:4:2]

# print(ans)

# s= "i am a cOdEr."

# ans = s.endswith("er. ")
# ans = s.capitalize()
# ans = s.replace("coder", "Trainer")
# ans = s.replace("a", "o", 1)
# ans = s.find("a")
# ans = s.swapcase()
# ans = s.count("a")

# print(ans)


# name = input("Enter your name: ")

# print(f"Name = {name}")
# print(f"Length of Name = {len(name)}")

# ans = name.count("a")
# print(f"Count of a = {ans}")

# a = input("Enter a word = ").lower()
# print(a)
# rev = a[::-1]

# print(a == rev)


# age = 52

# if(age < 18 ):
#     print("Minor")
# elif(age >= 18 and age < 60):
#     print("ADULT")
# else:
#     print("Senior Citizen")



# color = "pink"

# if(color == "red"):
#     print("STOP")
# elif(color == "green"):
#     print("GO")
# elif(color == "yellow"):
#     print("READY TO GO")
# else:
#     print("Invalid Color")


# n = 5

# if(n % 2 == 0):
#     print("Even Number")
# else:
#     print("Even Number")


# username = "Shivam"

# if(" " in username):
#     print("Invalid Username")
# elif(len(username) < 4):
#     print("Too Short")
# else:
#     print("Username Accepted")


# for i in range(3000000):
#     print("Hello World")


# for i in range(1, 11, 3):
#     print(i)

# for i in range(2, 101, 2):
#     print(i)

# for i in range(100, 0, -1):
#     print(i)


# n = int(input("Enter any number: "))
# for i in range(1, 11):
#     mul = n * i
#     print(f"{n} x {i} = {mul}")

# i = 2
# while(i <= 100):
#     print(i)
#     i+=2


# for i in range(5):
#     if i == 3:
#         continue
        
#     print(i)


n = int(input("Enter a number: "))

total = 0
for i in range(1, n+1):
    total = total + i
    
print(total)