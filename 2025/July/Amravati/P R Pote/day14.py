


# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None

# # Node1 = Node(12)
# # Node2 = Node(24)
# # Node3 = Node(39)

# # Node1.next = Node2
# # Node2.next = Node3

# # # Insert an element at the beginning
# # head = Node(5)
# # head.next = Node1

# # NodeMid = Node(17)
# # Node1.next = NodeMid
# # NodeMid.next = Node2

# # NodeEnd = Node(99)
# # Node3.next = NodeEnd

# # NodeMid.next = Node3


# # currentNode = head
# # print(currentNode)
# # while currentNode != None:
# #     print(currentNode.data, end=" -> ")
# #     # print(currentNode.data, currentNode.next, sep=" | ")
# #     currentNode = currentNode.next

# # print(None)


# # stk = []

# # stk.append(10)
# # stk.append(30)
# # stk.append(50)
# # stk.append(80)

# # print("Stack:", stk)

# # a = stk.pop()
# # b = stk.pop()
# # print(a)
# # print(b)
# # print("After Pop Stack:", stk)

# # print(stk[-1])
# # print(len(stk) == 0)



# class Stack:
#     def __init__(self):
#         self.items = []

#     def append_Stack(self, data):
#         self.items.append(data)
    
#     def pop_Stack(self):
#         if not stk.is_Empty():
#             return self.items.pop()
#         else:
#             print("Stack is Empty!")

    
#     def peek_Stack(self):
#         if(not stk.is_Empty()):
#             return self.items[-1]
#         else:
#             print("Stack is Empty!")
    
#     def is_Empty(self):
#         return len(self.items) == 0


#     def display(self):
#         print(f"Stack: {self.items}")
#         print(f"Peek (Top Element): {stk.peek_Stack()}")

# stk = Stack()

# stk.append_Stack(40)
# stk.append_Stack(10)
# stk.append_Stack(670)
# stk.append_Stack(320)
# stk.append_Stack(409)

# # print(stk)
# # stk.display()
# stk.pop_Stack()
# # stk.display()

# # a = stk.peek_Stack()

# # print(a)

# stk.display()
# # print(stk.is_Empty())
