
# # # from collections import deque

# # # dq = deque()

# # # dq.append(9)
# # # dq.append(76)
# # # dq.append(309)
# # # dq.appendleft(999)
# # # print(f"Original Deque = {dq}")

# # # dq.pop()
# # # dq.popleft()

# # # dq[-1]
# # # len(dq) == 0
# # # print(f"Modified Deque = {dq}")


# from collections import deque

# dq = deque()


# # Q1
# # dq.append(10)
# # dq.append(20)
# # dq.appendleft(5)

# # dq.pop()

# # print(dq)



# # # Q2

# n = "Madam"
# dq = deque(n)
# print(len(dq))

# print(dq)
# flag = False
# while len(dq) > 1:
#     if dq.pop() != dq.popleft():
#         flag = False
#     else:
#         flag = True

# if(flag == True):
#     print(f"{n} is Palindrome")
# else:
#     print(f"{n} is Not a Palindrome")



class Node:
    def __init__(self, node, left=None, right=None):
        self.node = node
        self.left = left
        self.right = right

root = Node(2)
root.left = Node(7)
root.right = Node(5)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(4)
root.right.right = Node(9)


# print(root.node)
# print(root.left.node)

def preOrder_Traversal(node):
    if(node):
        preOrder_Traversal(node.left)
        preOrder_Traversal(node.right)
        print(node.node, end=" ")

preOrder_Traversal(root)