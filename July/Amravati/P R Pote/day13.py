

# # # def merge_Sort_Fn(arr):

# # #     if(len(arr) <= 1):
# # #         return arr

# # #     mid = len(arr) // 2
# # #     left = merge_Sort_Fn(arr[:mid])
# # #     right = merge_Sort_Fn(arr[mid:])

# # #     return merge(left, right)

# # # def merge(left, right):
# # #     result = []
# # #     i = 0 
# # #     j = 0

# # #     while(i < len(left) and j < len(right)):
# # #         if(left[i] < right[j]):
# # #             result.append(left[i])
# # #             i += 1

# # #         else:
# # #             result.append(right[j])
# # #             j += 1

# # #     while(i < len(left)):
# # #         result.append(left[i])
# # #         i += 1

# # #     while(j < len(right)):
# # #         result.append(right[j])
# # #         j += 1

# # #     return result


# # def quick_Sort_Fn(arr):

# #     if(len(arr) <= 1):
# #         return arr

# #     pivot = arr[0]
# #     small = []
# #     big = []

# #     for i in range(1, len(arr)):
# #         if(arr[i] < pivot):
# #             small.append(arr[i])

# #         else:
# #             big.append(arr[i])

# #     return quick_Sort_Fn(small) + [pivot] + quick_Sort_Fn(big)

# # # arr = [249, 186, 1, 993, 885, 213, 545, 674]
# # arr = [6, 8, 4, 1, 10, 24, 7, 12]

# # # mergeSort = merge_Sort_Fn(arr)
# # # print(mergeSort)

# # quickSort = quick_Sort_Fn(arr)
# # print(quickSort)


# # arr = [2, 4, 6, 7, 8, 9, 10, 12, 14, 15, 17, 19, 20, 21]

# # sum = 0
# # for i in range(12):
# #     sum += arr[i]

# # print(sum)



# arr = [2, 4, 6, 7, 8, 9, 10, 12, 14, 15, 17, 19, 20, 21]

# sum = [0] * (len(arr) + 1)
# for i in range(len(arr)):
#     sum[i+1] = sum[i] + arr[i]

# newSum = sum[14] - sum[8]
# print(newSum)

