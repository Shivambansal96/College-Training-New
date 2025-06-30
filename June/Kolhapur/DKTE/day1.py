# # # Sum of 2 numbers
# # a = int(input("Enter a number = "))
# # b = int(input("Enter another number = "))

# # sum = a + b
# # print(f"Sum = {sum}")


# # # Area 
# # side = int(input("Enter a number = "))

# # area = side * side
# # print(f"Area = {area}")


# # # Average of 2 numbers
# # a = float(input("Enter a number = "))
# # b = float(input("Enter another number = "))

# # avg = (a + b) /2
# # print(f"Average = {avg}")


# # Max of 2 numbers
# a = int(input("Enter a number = "))
# b = int(input("Enter another number = "))

# # if(a >= b):
# #     print("True")
# # else:
# #     print("False")

# print(a >= b)




# originalWord = "I am madam" # input

# # reversedWord = originalWord[len(originalWord) - 1: - len(originalWord) - 1: -1]

# reversedWord = originalWord[::-1]

# if(originalWord == reversedWord):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")








# Conditional Statements

# marks = 35
# grade = None
# flag = False

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# elif(marks >= 60 and marks < 70):
#     grade = "D"
# elif(marks >= 50):
#     grade = "Pass"
# else:
#     # print(f"Marks = {marks}")
#     flag = True
#     grade = "FAIL"
    

# if(flag == False):
#     print(f"GRADE = {grade}")
# else:
#     print(f"GRADE = {grade}, MARKS + {marks}")


# # Max of 3 numbers
# a = 10
# b = 20
# c = 30

# if( a > b and a > c):
#     print(a)
# elif(b > c):
#     print(b)
# else:
#     print(c)













# # # # # SET QUESTION
# text1 = "Python is a great programming language"
# text2 = "Many developers love the Python language"

# # Convert strings to lowercase and split into words
# words1 = set(text1.lower().split())
# words2 = set(text2.lower().split())

# print(words1)
# print(words2)

# # 1. Words that appear in both texts
# # common_words = words1 and words2
# print(words1.intersection(words2))


# # 2. Words unique to the first text
# unique_to_text1 = words1 - words2



# # 3. Total number of unique words across both texts
# all_unique_words = words1 | words2
# total_unique_count = len(all_unique_words)

# # Output
# # print("Common words:", common_words)
# # print("Unique to text1:", unique_to_text1)
# # print("Total unique words:", total_unique_count)
