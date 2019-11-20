# In order traversal [MEDIUM] 
Return array of in order traversal nodes. Recursive and iterative.

## Solution

```
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        traversed = []
        while stack:
            head = stack[-1]
            if(head.left):
                stack.append(head.left)
                head.left = None
                continue
            head = stack.pop()
            traversed.append(head.val)
            if(head.right):
                stack.append(head.right)
                head.right = None
                continue
        return traversed

```