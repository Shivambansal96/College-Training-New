originalList = [input(), input(), input(), input()]
copiedList = originalList.copy()

copiedList.reverse()

if(originalList == copiedList):
    print("Palindrome List")
else:
    print("Not a Palindrome List")
