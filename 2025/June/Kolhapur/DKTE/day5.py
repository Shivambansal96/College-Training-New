

# def add(x, y):
#     return x + y

# add(4, 6)

# add = lambda x, y: x > y

# if(add(4, 5) == True):
#     Max = x
# else:
#     Max = y





# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("Result:", result)

# except ZeroDivisionError:
#     print("Error: You can't divide by zero!")

# except ValueError:
#     print("Error: Invalid input, please enter a valid number.")

# except Exception as e:
#     print(f"unexpected ERROR")

# else:
#     print(f"NO ERROR !!!")

# finally:
#     print(f"I will always be executed.")


import numpy as np


# x = [1, 2, 7, 4, 5 ]

# myArr = np.array(x, np.int8)
# myArr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(myArr.shape)
# print(myArr2.shape)

# print(myArr.dtype)
# print(myArr2.dtype)

# print(myArr.nbytes)
# print(myArr2.nbytes)


# print(myArr.size)
# print(myArr2.size)

# print(myArr.flat)
# print(myArr2.flat)

# for i in myArr2:
#     print(i)

# ar = np.zeros([3, 4])

# ar = np.linspace(0, 10, 5)

# ar = np.empty([3, 5])
# ar[2, 3] = 32

# print(ar)


# myArr = np.arange(1, 100)

# ar = myArr.reshape(33, 3)

# arr = ar.ravel()

# print("Reshaping", ar)
# print("ravel = ", arr)


# myArr = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])

# print(myArr.argmax(axis=0))



# # myArr2 = np.array([3, 2, 20])

# # arr = np.where(myArr==10)

# arr = np.nonzero(myArr)
# print(arr)


# # arr = myArr.argsort(axis=0)

# # print(myArr * myArr2)


import sys

py_ar = [1, 2, 3]
np_ar = np.array([py_ar])


py_ar_size = sys.getsizeof(py_ar) * len(py_ar)
np_ar_size = np_ar.itemsize * np_ar.size

print(py_ar_size)
print(np_ar_size)


myArr = np.array([[3, 2, 50], 
                  [10, 0, 3], 
                  [0, 2, 30]])

arr = np.sum(myArr)
print(arr)

ar = myArr.sum(axis=0)
print(ar)