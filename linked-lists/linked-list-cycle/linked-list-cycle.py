class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if(head is None):
            return False
        
        fastPointer = head
        
        while(head.next and fastPointer.next.next):
            fastPointer = fastPointer.next.next
            if(fastPointer == head):
                return True
            head = head.next
            if(fastPointer == None or fastPointer.next == None):
                return False
            
        return False