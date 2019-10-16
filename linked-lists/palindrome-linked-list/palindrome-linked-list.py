class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ## find mid node, reverse half list and compare
        if(head == None or head.next == None):
            return True
        start = head
        mid = head
        prev = head
        while(head and head.next):
            head = head.next.next
            #reverse list and track mid
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
            
        # if even number of elements in the list, skip the mid element
        if(head):
            mid = mid.next
        
        #prev would be first node in the first half of the reversed list
        while(mid):
            if(prev.val != mid.val):
                return False
            else:
                prev, mid = prev.next, mid.next
        return True