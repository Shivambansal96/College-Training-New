# GUESS A RANDOM NUMBER GAME


import random

n = int(input("Enter a Range you want = "))

difficultyLevel = input("Enter a Difficulty level(Easy, Medium, Hard) = ")
attempts = 0

if(difficultyLevel == 'Hard' or difficultyLevel == 'H'):
    attempts = 3
    print(f"You have {attempts} Attempts to Guess a Number")

elif(difficultyLevel == 'Medium' or difficultyLevel == 'M'):
    attempts = 5
    print(f"You have {attempts} Attempts to Guess a Number")

elif(difficultyLevel == 'Easy' or difficultyLevel == 'E'):
    attempts = 10
    print(f"You have {attempts} Attempts to Guess a Number")

else:
    print("Invalid Input!")
    difficultyLevel = input("Enter a Difficulty level(Easy, Medium, Hard) = ")

randomNum = random.randint(1, n)

guess = 0
tries = 0

input("Press Enter to Start the Game")

while (attempts > 0):
    tries +=1
    guess = input("Enter an int to play or 'Q' to Quit = ")

    if(guess == 'Q' or guess =='q' or guess == 'Quit'):
        break

    else:
        guessNum = int(guess)

        if(guessNum < randomNum):
            print("The actual number is greater")

        elif(guessNum > randomNum):
            print("The actual number is lower")

        else:
            print("Congrats You guessed it!")
            break
    attempts -= 1

    if(attempts == 1):
        print("!! ONE LAST CHANCE !!")

print("----------- GAME OVER -----------")
print(f"The correct number was {randomNum}")
