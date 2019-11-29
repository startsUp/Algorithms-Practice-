
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)
    def helper(self, root):
        if root == None:
            return
        
        if root.left:
            rightMost = self.helper(root.left)
            if rightMost: # flatten
                rightMost.right = root.right
                root.right = root.left
                root.left = None
            
        if root.right:
            root = self.helper(root.right)

        return root

x = TreeNode(1)
x.left = TreeNode(2)
x.right = TreeNode(4)
x.left.left = TreeNode(3)
x.left.right = TreeNode(5)
x.left.left = TreeNode(2)
x.right.left = TreeNode(4)

s = Solution()
s.flatten(x)