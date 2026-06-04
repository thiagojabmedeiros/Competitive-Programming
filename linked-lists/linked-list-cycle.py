class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

def hasCycle(ll: Node):
    index = -1
    hashIndex = {}
    curr = ll
    while curr:
        if curr in hashIndex:
            return True
        index += 1
        hashIndex[curr] = index
        curr = curr.next
    return False