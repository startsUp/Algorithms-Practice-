class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def insert(root, val):
    if root == None:
        return TreeNode(val=val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root

bst = []
def preorder(root):
    if root == None:
        bst.append(None)
        return
    bst.append(root.val)
    preorder(root.left)
    preorder(root.right)

def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: int
    :type q: int
    :rtype: TreeNode
    """
    parent_val = root.val

    if p < parent_val and q < parent_val:
        return lowestCommonAncestor(root.left, p, q)

    if p > parent_val and q > parent_val:
        return lowestCommonAncestor(root.right, p, q)

    return root
        
def height(root, val):
    if root.val == val:
        return 0
    
    if val < root.val:
        return (height(root.left, val) + 1)
    else:
        return (height(root.right, val) + 1)

l = [4, 2, 7, 1, 3, 5]
p = 1
q = 2
root = None
for val in l:
    root = insert(root, val)
preorder(root)

print bst
lca = lowestCommonAncestor(root, p, q)
print lca.val
h1 = height(lca, p)
h2 = height(lca, q)
print h1, h2
print h1 + h2