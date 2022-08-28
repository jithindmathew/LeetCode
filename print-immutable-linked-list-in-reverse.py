# 1265

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
def printLinkedListInReverse(head):
    if head.next:
        printLinkedListInReverse(head.next)
    print(head.val)
        

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(a)):
    a[i] = Node(a[i])
for i in range(len(a) - 1):
    a[i].next = a[i + 1]
    
    
printLinkedListInReverse(a[0])
    
