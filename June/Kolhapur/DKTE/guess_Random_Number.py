
import random

def guess_num():
    n = 100
    randomNum = random.randint(1, n)

    attempts = 0
    diffLevel = input("Enter the mode of difficulty (Easy, Medium, Hard) = ")

    if(diffLevel == "Easy"  or diffLevel == "e" or diffLevel == "E" or diffLevel == "easy"):
        attempts = 10
        print(f"You have {attempts} attempts left.")

    elif(diffLevel == "Medium"  or diffLevel == "m" or diffLevel == "M" or diffLevel == "medium"):
        attempts = 5
        print(f"You have {attempts} attempts left.")

    elif(diffLevel == "Hard"  or diffLevel == "h" or diffLevel == "H" or diffLevel == "hard"):
        attempts = 3
        print(f"You have {attempts} attempts left.")

    else:
        print("Invalid input")

    input("Press Enter to start the game.")

    while(attempts != 0):
        userInput = input(f"Guess a random number between 1 and {n} = ")

        if(userInput == "q" or userInput == "Quit" or userInput == "quit" or userInput == "Q"):
            print("Ok Bye!")
            break

        else:
            userInput = int(userInput)
            if(userInput == randomNum):
                print(f"You win 🎉")
                break

            elif(userInput < randomNum):
                print(f"Guess a higher number.")

            else:
                print(f"Guess a lower number.")

            attempts -= 1

guess_num()


while(True):
    pA = input(" \t \t \t Do you want to play again ? \t \t \t")

    if(pA == "yes"):
        guess_num()
    else:
        print("you quit!")
        break
