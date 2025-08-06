
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n - 1)

# fileName = open("demo.txt")

# data = fileName.readline()
# print(data)

# fileName.close()


# fileName = open("demo.txt", "a")
# fileName.write("\nI got Deleted!!!")

# fileName.close()



# fileName = open("demo.txt", "a")
# fileName.write("\nI got Deleted!!!")

# fileName.close()


# import os

# os.rename("dim.txt", "demo.txt")



fileName = open("practice.txt", "w")
fileName.write("Hi Everyone. \nWe are learning File Handling I/o\nusing python.\nI like programming in Python.")

fileName.close()
# ----------------------- #
# ---------- OPEN, READ  AND MODIFY------------- #

fileName = open("practice.txt")
data = fileName.read()

data = data.lower()
data2 = data.replace("python", "javaScript")

# print(data)
# print()
# print(data2)
fileName.close()

# ---------- WRITE THE CHANGED / REPLACED DATA ------------- #

fileName = open("practice.txt", "w")
fileName.write(data2)