class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def mergeTrees(t1, t2):
    if (t1 is not None and t2 is not None):
        t1.val += t2.val
        t1.left = mergeTrees(t1.left, t2.left)
        t1.right = mergeTrees(t2.right, t2.right)
        return t1
    else:
        return t1 or t2

