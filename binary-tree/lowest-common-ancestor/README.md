## Question [Medium]
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

## Solution
- Inorder traversal => Keep track of the lowest common ancestor once p or q is found.
- Only update the LCA when you are going up a level (if last LCA is a descendent of the current node)
- When the other (p or q) node is found, break and return the last set LCA

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    current = root  
    stack = []
    level, lcaLevel = 0, 0 # track the current level and of the last ancestor found
    lca = None
    qFound, pFound = False, False
    while True: 
        if current is not None: 
            level+=1
            stack.append(current) 
            pFound = pFound or current.val == p.val
            qFound = qFound or current.val == q.val
            if (pFound and qFound):
                break
            elif((pFound or qFound) and lca is None): # set the ancestor to p or q, whichever is found first
                lca = current
                lcaLevel = level
            current = current.left  
        elif(stack): 
            current = stack.pop() 
            level-=1
            if(current.left and lca is not None and level < lcaLevel): # only update the LCA if lca is a descendant of the current node
                lca = current
                lcaLevel = level
            current = current.right
        else: 
            break
    return lca
```