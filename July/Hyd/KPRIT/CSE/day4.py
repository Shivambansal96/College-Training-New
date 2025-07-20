# myList = [4]
# myTup = (2,)


# print(type(myList))
# print(type(myTup))


# myTup = ("A", "B", "C", "A" , "C" , "D")
# print(myTup.count("A"))

# print(sorted(myTup))

# myList = list(myTup)
# myList.sort()
# print(myList)


# mySet = {1, 2, 3, 4, 2, 1, 2}
# mySet = set()
# print(mySet)
# print(type(mySet))


# mySet = {1, 2, 3, 4, 2, 1, 2}
# mySet.add(54)
# # mySet.remove(2)
# # mySet.clear()
# mySet.pop()
# print(mySet)


# mySet1 = {1, 2, 3}
# mySet2 = {3, 4, 5}

# AUB = mySet1.union(mySet2)
# ANB = mySet1.intersection(mySet2)

# print(AUB)
# print(ANB)
# mySet2.remove(1)
# mySet2.discard(1)

# print(mySet2)


# mySet = {"C++", "C", "Python", "Java", "Js", "Js", "Java", "C++"}
# print(len(mySet))

text1 = "Python is a great programming language"
text2 = "Many developers love the python language"

myList1 = text1.lower().split()
myList2 = text2.lower().split()

mySet1 = set(myList1)
mySet2 = set(myList2)

aNb = mySet1.intersection(mySet2)

print(f"Intersection = {aNb}")

diff = mySet1.difference(mySet2)

print(f"Difference = {diff}")

aUb = mySet1.union(mySet2)
symmDiff = mySet1.symmetric_difference(mySet2)

print(f"Union = {aUb}")
print(f"Symmetric DIfference = {symmDiff}")

a = "-".join(symmDiff)
print(a)