# import random


# def guess_Random_Num():
#     randomNum = random.randint(1, 10)

#     diffLevel = input("Enter the mode of Difficulty (Easy, Medium, Hard) = ")

#     attempts = 0
#     if(diffLevel == "Easy"):
#         attempts = 10
#         print(f"You have {attempts} attempts")

#     elif(diffLevel == "Medium"):
#         attempts = 5
#         print(f"You have {attempts} attempts")

#     elif(diffLevel == "Hard"):
#         attempts = 3
#         print(f"You have {attempts} attempts")

#     else:
#         print("Invalid Input")
#         diffLevel = input("Enter the mode of Difficulty (Easy, Medium, Hard) = ")

#     input("Press Enter to START the game.")

#     while (attempts != 0):
#         userInput = input("Enter a random number between 1 and 10 = ")

#         if(userInput == "Q" or userInput == "Quit"):
#             print("You Quit the Game!")
#             break
        
#         else:
#             userInput = int(userInput)

#             if(userInput == randomNum):
#                 print("You Win 🎉")
#                 break
#             elif(userInput > randomNum):
#                 print("Your Number is too high!")
#             else:
#                 print("Your Number is lower")


#             attempts -= 1
#         if(attempts == 1):
#             print("FINAL TRY!!!")


# guess_Random_Num()

# while(True):
#     pA = input("\t\t\t\t\t Do you want to Play Again? \t\t\t\t")

#     if(pA == "Yes"):
#         guess_Random_Num()
#     else:
#         print("Bhaad meh ja! MAT KHEL")
#         break
