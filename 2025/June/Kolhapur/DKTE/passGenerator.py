import random
import string

n = int(input("Enter the length of password you want to generate = "))
if(n == 0):
    raise ValueError("Password length cannot be 0")

allCharacter = string.ascii_letters + string.digits

randomPass = ""

for i in range(n):
    randomPass += random.choice(allCharacter)

print (randomPass)