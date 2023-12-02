# def isPowerofTwo( n):
#     if n % 2 != 0:
#         return False
#     else:
#         num = n // 2
#         if num % 2 == 0:
#             return True
#         else:
#             return False
#
# print(isPowerofTwo(26500))

# def immediateSmaller(arr):
#     # code here
#     i = 0
#     j = 1
#
#     while j < len(arr):
#         if arr[i] > arr[j]:
#             arr[i] = arr[j]
#         else:
#             arr[i] = -1
#         i+=1
#         j+=1
#
#     arr[-1] = -1
#     return arr
#
# print(immediateSmaller([5, 6, 2, 3, 1, 7]))

# def getMinMax(a):
#     a.sort()
#     arr = []
#     arr.append(a[0])
#     arr.append(a[-1])
#     return arr
#
# print(getMinMax([3, 2, 1, 56, 10000, 167]))

# class Node:
#     # Function to initialize the node object
#     def __init__(self, data):
#         self.data = data  # Assign data
#         self.next = None  # Initialize
#         # next as null
#
#
# # Linked List class
# class LinkedList:
#
#     # Function to initialize the Linked
#     # List object
#     def __init__(self):
#         self.head = None
#
#     def insert(self, val):
#         if self.head == None:
#             self.head = Node(val)
#         else:
#             new_node = Node(val)
#             temp = self.head
#             while (temp.next):
#                 temp = temp.next
#             temp.next = new_node
#
#     def display(self, node):
#         while (node is not None):
#             print(node.data, end=" ")
#             node = node.next
#
#
# def fractionalNodes(head, k):
#
#     N = 1
#     temp = head
#     print(type(temp))
#     while temp:
#         temp = temp.next
#         N += 1
#     temp = head
#     i = 1
#     N-=1
#     value = N//k
#     while temp:
#         if i == value:
#             return temp
#         else:
#             temp = temp.next
#             i += 1
#
#
#
# if __name__ == '__main__':
#     lis = LinkedList()
#     n = 15
#     arr = [88 ,57, 44 ,92 ,28 ,66, 60, 37 ,33, 52 ,38 ,29, 76, 8 ,75 ]
#     k = 2
#     # head = createList(arr, n)
#     for i in range(0, len(arr)):
#         lis.insert(arr[i])
#     ans = fractionalNodes(lis.head, k)
#     print(ans.data)

def printFibb(n):
    # your code here
    a = 1
    b = 1
    arr = []
    i = 0
    while i < n:
        if i < 2:
            arr.append(a)
        else:
            c = a + b
            a = b
            b = c
            arr.append(c)
        i += 1
    return arr

print(printFibb(10))