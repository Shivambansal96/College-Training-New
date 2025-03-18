

# # # # # # GUESS A RANDOM NUMBER

import random

def guess_Game():
    
    randomNum = random.randint(1, 100)
    guessNum = 0
    attempts = 0

    diffLevel = input("Enter a difficulty level(Easy, Medium, Hard) = ")

    def set_Difficulty(diffLevel, attempts):
        
        if(diffLevel == "Hard"):
            attempts = 3
            print(f"You have {attempts} Chances to guess the Correct Number")

        elif(diffLevel == "Medium"):
            attempts = 5
            print(f"You have {attempts} Chances to guess the Correct Number")

        elif(diffLevel == "Easy"):
            attempts = 10
            print(f"You have {attempts} Chances to guess the Correct Number")

        else:
            print("Invalid Input!")

        return attempts

    attempts = set_Difficulty(diffLevel, attempts)


    while (attempts > 0):
        guessNum = input("If you want to play Enter a number or Enter 'Q' to Quit = ")

        if(guessNum == 'Q'):
            break

        else:
            guessNum = int(guessNum)
            if(guessNum > randomNum):
                print("Your guess is higher than the actual number")
            elif(guessNum < randomNum):
                print("Your guess is lower than the actual number")
            else:
                print("SUCCESS - You guessed it Correct!")

        attempts -= 1

        if(attempts == 1):
            print("LAST TRY!")
    print("---------- GAME OVER ---------------")

guess_Game()

while True:
    playAgain = input("\t\tDo you want to play again?\t")

    if(playAgain == "Y" or playAgain == "Yes"):
        guess_Game()
    else:
        break







