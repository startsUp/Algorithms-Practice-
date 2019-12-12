"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None: return []
        stack = [root]
        ans=[]
        while stack:
            head = stack[-1]
            if not head.children:
                ans.append(head.val)
                stack.pop()
            else:
                for i in range(len(head.children)):
                    stack.append(head.children[len(head.children)-i-1])
                head.children = []
        
        return ans
