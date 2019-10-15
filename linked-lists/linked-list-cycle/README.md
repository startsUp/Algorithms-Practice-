## Question

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

> Implement it using **O(1)** memory

## Solution

Use two pointers. Fast pointer and slow pointer. Fast pointer moves 2 steps for every one step that slow pointer moves.

```
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
```
