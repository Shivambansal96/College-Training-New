

import random

def guess_random_number():
    randomNum = random.randint(1, 100)

    input("Press Enter to Start.")
    diffLevel = input("Enter the mode of difficulty(Easy, Medium, Hard) = ").lower()

    if(diffLevel == "easy" or diffLevel == "e"):
        attempts = 10
        print(f"You get {attempts} attempts.")

    elif(diffLevel == "medium" or diffLevel == "m"):
        attempts = 5
        print(f"You get {attempts} attempts.")

    elif(diffLevel == "hard" or diffLevel == "h"):
        attempts = 3
        print(f"You get {attempts} attempts.")

    else:
        print("Invalid Input")

    while attempts != 0:
        userInput = int(input("Guess a random Number = "))

        if(randomNum == userInput):
            print("Congratulations 🎉")
            break
        
        if(attempts > 1):
            if(userInput > randomNum):
                print("Guess a lower number")
            else:
                print("Guess a higher number")

        attempts -= 1

        if(attempts == 3):
            print("\t\t\t\t\t\tLast 3 tries left")
        
        if(attempts == 1):
            print("\t\t\t\t\t\t\tFINAL CHANCE!!")

    else:
        print("You lost! 🥲")
        print(f"The correct number was {randomNum}")

guess_random_number()


while True:
    pA = input("\n\t\t\tDo you want to play Again? \t").lower()

    if(pA == "yes" or pA == "y"):
        guess_random_number()
    elif(pA == "no" or pA == "n"):
        print("Bye Loser!")
        break
    else:
        print("Invalid Input")



