
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def recursiveReverseList(head: ListNode):
    # 1 -> 2 -> 3 -> null
    if head is None or head.next is None: 
        return [head, head]
    else:
        
        rHead, tail = recursiveReverseList(head.next)
        tail.next = head
        head.next = None
        return [rHead, head]

def printList(head: ListNode):
    while (head):
        print(head.val)
        head = head.next

x = ListNode(1)
y = ListNode(2)
z = ListNode(3)
x.next = y
y.next = z
s, t = recursiveReverseList(x)
printList(s)