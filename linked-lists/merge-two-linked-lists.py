class Node:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = None

l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(4)

l2 = Node(1)
l2.next = Node(3)
l2.next.next = Node(5)

def mergeTwoLists(list1: Node, list2: Node):
    mL = Node()
    tail = mL
    while list1 and list2:
        if list1.val > list2.val:
            tail.next = list2
            list2 = list2.next
        else:
            tail.next = list1
            list1 = list1.next
        tail = tail.next
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    return mL.next
mergeTwoLists(l1, l2)