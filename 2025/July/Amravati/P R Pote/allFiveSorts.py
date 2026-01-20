
def bubble_Sort(myArr):

    n = len(myArr) - 1
    for i in range(n):
        for j in range(n - i):
            if(myArr[j] > myArr[j+1]):
                myArr[j], myArr[j+1] = myArr[j+1], myArr[j]

    return myArr

def selection_Sort(myArr):
    n = len(myArr) - 1

    for i in range(n):
        minIndex = i
        for j in range(i+1, n+1):
            if(myArr[j] < myArr[minIndex]):
                minIndex = j
        if(minIndex != i):
            myArr[i], myArr[minIndex] = myArr[minIndex], myArr[i]

    return myArr

# METHOD 1
def insertion_Sort(myArr):
    for i in range(1, len(myArr)):
        for j in range(i-1, -1, -1):
            if(myArr[j] > myArr[j + 1]):
                myArr[j], myArr[j+1] = myArr[j+1], myArr[j]
            else:
                break

    return myArr

# METHOD 2
def insertion_Sort(myArr):
    for i in range(1, len(myArr)):
        j = i - 1
        while(myArr[j] > myArr[j + 1] and j >= 0):
            myArr[j], myArr[j+1] = myArr[j+1], myArr[j]
            j -= 1

    return myArr

def merge_Sort(myArr):
    if len(myArr) <= 1:
        return myArr
    mid = len(myArr) // 2
    left = merge_Sort(myArr[:mid])
    right = merge_Sort(myArr[mid:])
    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0
    result = []

    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    while(i < len(left)):
        result.append(left[i])
        i+=1

    while(j < len(right)):
        result.append(right[j])
        j+=1

    return result


def quick_Sort(myArr):

    if(len(myArr) <= 1):
        return myArr
    
    pivot = myArr[0]
    smallArr = []
    bigArr = []

    for i in range(1, len(myArr)):
        if(myArr[i] <= pivot):
            smallArr.append(myArr[i])
        else:
            bigArr.append(myArr[i])

    return quick_Sort(smallArr) + [pivot] +  quick_Sort(bigArr)

myArr = [3, 4, 24 , 6, 75, 42, 2, 1, 45, 87]
# myArr = ["a", "d", "c", "p", "k"]
bubbleSortedArr = bubble_Sort(myArr)
selectionSortedArr = selection_Sort(myArr)
insertionSortedArr = insertion_Sort(myArr)
mergeSortedArr = merge_Sort(myArr)
quickSortedArr = quick_Sort(myArr)

print(bubbleSortedArr)
print(selectionSortedArr)
print(insertionSortedArr)
print(mergeSortedArr)
print(quickSortedArr)
