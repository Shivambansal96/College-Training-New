# # Bubble Sort:


# # def bubble_Sort_Fn(arr):
# #     n = len(arr) - 1
# #     for i in range(n):
# #         for j in range(n-i):
# #             if(arr[j+1] < arr[j]):
# #                 arr[j], arr[j+1] = arr[j+1] , arr[j]

# #     return arr

# # def insertion_Sort_Fn(arr):

# #     # for i in range(1, len(arr)):
# #     #     for j in range(i-1, -1, -1):
# #     #         if(arr[j] > arr[j+1]):
# #     #             arr[j], arr[j+1] = arr[j+1], arr[j]

# #     n = len(arr) - 1

# #     for i in range(1, n):
# #         for j in range(i, 0, -1):
# #             if(arr[j] < arr[j-1]):
# #                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
    

# #     return arr

# def selection_Sort_Fn(arr):

#     n = len(arr) - 1

#     for i in range(n):
#         minIndex = i
#         for j in range(i+1, n):
#             if(arr[j] < arr[minIndex]):
#                 minIndex = j
#         # if(minIndex != i):
#                # arr[i], arr[minIndex] = arr[minIndex], arr[i]

# arr = [22, 1, 16, 58, 120 , 12]
# # arr = ["c", "d", "a", "g", "f", "n", "e"]
# # bubbleSort = bubble_Sort_Fn(arr)
# insertionSort = insertion_Sort_Fn(arr)
# selectionSort = selection_Sort_Fn(arr)
# # print(f"Bubble Sorted List = {bubbleSort}")
# print(f"Insert Sorted List = {insertionSort}")
# print(f"Selection Sorted List = {selectionSort}")

nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
sums = [0] * (len(nums)+1)
for i in range(len(nums)):
    sums[i+1] = sums[i] + nums[i]

rangeSum = sums[10] - sums[5]

print(sums)
print(rangeSum)