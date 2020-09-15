## Linked List Cycle II [Medium]
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?

 
```
Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

## Solution
 - Use fast and slow pointer to detect if there is a cycle
 - After cycle has been detected the distance `head - start` will be equal to `start - fast` so we just move slow to head and increment both pointers by 1 until they are equal. This will give us the start of the cycle.  

```python
def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None
```