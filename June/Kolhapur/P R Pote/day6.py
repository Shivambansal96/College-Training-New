
n = 5
for rows in range(1, n+1):
    for stars in range(1, rows+1):
        print("* ", end="")
    print()
print("--------------------------")

n = 5
for rows in range(1, n+1):
    for stars in range(1, rows+1):
        print(stars, end="")
    print()
print("--------------------------")

n = 5
for rows in range(1, n+1):
    for stars in range(1, rows+1):
        print(rows, end="")
    print()
print("--------------------------")

n = 5
for rows in range(1, n+1):
    for stars in range(1, rows+1):
        print(chr(rows + 64), end="")
    print()
print("--------------------------")


n = 5
for rows in range(1, n+1):
    for stars in range(1, rows+1):
        print(chr(stars + 64), end="")
    print()
print("--------------------------")

# n = 5
# for rows in range(n, 0, -1):
#     for spaces in range(rows-1, 0, -1):
#         print(" ", end="")

#     for stars in range(n, rows-spaces, -1):
#         print(rows, end="")

#     print()


# n = 5

# for rows in range(1, n+1):
#     for cols in range(1, n+1):
#         if(rows == 1 or rows == n or cols == 1 or cols == n):
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()


t1 = "Python is a good python language"

words = t1.split()

for i in range(len(words)):
    words[i] = words[i].lower()

freq = {}

for i in range(len(words)):
    if words[i] in freq:
        freq[words[i]] += 1
    else:
        freq[words[i]] = 1

print(freq)
