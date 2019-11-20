## Question [Medium]
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
```
    3
   / \
  9  20
    /  \
   15   7
```
return its level order traversal as:
```
[
  [3],
  [9,20],
  [15,7]
]
```
## Solution
Starting with root, append and store it in array. For each level append its left and right node to current level array and repeat.


```
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        nodesInCurrentLevel = [root]
        while nodesInCurrentLevel:
            ans.append([n.val for n in nodesInCurrentLevel])
            nextLevel = []
            for node in nodesInCurrentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            nodesInCurrentLevel = nextLevel
        
        return ans

```