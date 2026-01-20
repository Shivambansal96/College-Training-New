import string
import random

allCharacters = string.ascii_letters + string.digits + string.punctuation
passLength = int(input("Enter the length of password you need = "))

randomPass = ""
for i in range(len(passLength)):
    randomPass += random.choice(allCharacters)
    
print(randomPass)