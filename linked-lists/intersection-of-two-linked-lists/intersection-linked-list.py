class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
    
        if(headA == None or headB == None):
            return None
        
        # need to find length of both linked lists
        l1 = 0
        l2 = 0
        s1 = headA
        s2 = headB
        while(headA.next or headB.next):
            if(headA.next):
                l1+=1
                headA = headA.next
            if(headB.next):
                l2+=1
                headB = headB.next
        
     
        
        # shift the bigger linked list abs(l1-l2) to the right
        x = abs(l1-l2)
        shift = s1 if l1 > l2 else s2
        while(x!=0):
            shift = shift.next
            x-=1
        s1 = shift if l1 > l2 else s1
        s2 = shift if l2 > l1 else s2
        
        while(s1 != s2):
            s1, s2 = s1.next, s2.next
        
        return s1