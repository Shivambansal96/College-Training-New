

# # nums = [34, 83, 98, 33, 14, 34, 56]
# # i = 0
# # while(i < len(nums)):
# #     if(nums[i] == 98):
# #         print(nums[i], "FOUND AT INDEX = ", i)
# #         break
# #     else:
# #         print("finding...")
# #     i += 1


# nums = [34, 83, 98, 33, 14, 34, 56]

# for i in nums:
#     if(i == 98):
#         print("FOUND")
#         break
#     else:
#         print("finding")

# print("LOOP ENDS")


# n = int(input())
# for i in range(1, 11):
#     print(i*n)

n = 5
i = 1
sum = 0
while(i <= n):
    sum = sum + i
    i += 1
    
print("Sum = ", sum)