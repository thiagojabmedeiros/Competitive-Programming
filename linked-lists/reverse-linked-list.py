class Node:
    def __init__(self):
        self.value = None
        self.next = None

    def display(self):
        curr = self
        res = ""
        while curr is not None:
            res += str(curr.value) + " -> "
            curr = curr.next
        return res
    
def reverse(list):
    prev = None
    curr = list
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev.display

ll = Node()
ll.value = 1

ll.next = Node()
ll.next.value = 2

ll.next.next = Node()
ll.next.next.value = 3

ll.next.next.next = Node()
ll.next.next.next.value = 4

print(ll.display())