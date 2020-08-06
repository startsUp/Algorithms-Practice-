# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
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