class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # inorder traversal, stop when you find the kth element
        if root is None: return
        s = [root]
        while s:
            head = s.pop()
            if head.right:
                s.append(head.right)
                head.right = None
            
            if head.left:
                s.append(head)
                s.append(head.left)
                head.left = None
            else:
                k-=1
                
            if k == 0:
                return head.val
            
        return 0    