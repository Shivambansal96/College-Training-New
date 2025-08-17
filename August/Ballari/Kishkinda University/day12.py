# string = "ABCDCDCDC"
# sub_Str = "CDC"

# count =  0
# start = 0

# while True:
#     start = string.find(sub_Str, start)

#     print(f"SUB_Str at index = {start}")

#     if(start == -1):
#         break

#     count += 1
#     start += 1

# print(count)



s = "shivam bansal"

# print(s.capitalize())

newStr = ""
for i in range(len(s)):
    if(s[i-1] == " "):
        newStr += s[i].capitalize()

    else:
        newStr += s[i]
        
print(newStr)














