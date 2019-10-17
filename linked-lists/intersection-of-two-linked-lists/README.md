## Question 
Write a program to find the node at which the intersection of two singly linked lists begins.

### Example 1:

```
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
```

## Solution
- Find lengths of both linked lists
- Reset pointers to the start of the both linked list but shift the pointer for the larger linked list by |l2-l1|.
- Increment pointers until intersection node is found (pointers should be equal)


```
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
```