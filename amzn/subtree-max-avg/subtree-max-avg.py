"""

  Given an N-ary tree, find the subtree with the maximum average. Return the root of the subtree.
  A subtree of a tree is the node which have at least 1 child plus all its descendants. The average value of a subtree is the sum of its values, divided by the number of nodes.

"""
class TreeNode():
  def __init__(self, val):
    self.val = val
    self.right = None
    self.left = None

class NAryNode():
  def __init__(self, val):
    self.val = val
    self.children = None
  
def subtree_max_avg(root: TreeNode):
  maxAvg = (root, root.val)

  def get_subtree_avg(cur_root):
    nonlocal maxAvg
    if cur_root is None:
      return (0, 0)
    r_num, r_sum = get_subtree_avg(cur_root.right)
    l_num, l_sum = get_subtree_avg(cur_root.left)

    # calculate max 
    avg = (cur_root.val + r_sum + l_sum) / (r_num + l_num + 1)
    if avg > maxAvg[0]:
      maxAvg = (cur_root, avg)
    
    return (r_num + l_num + 1, cur_root.val + r_sum + l_sum)
  get_subtree_avg(root)
  return maxAvg[1]

def subtree_max_avg(root: NAryNode):
  maxAvg = (root, root.val)

  def get_subtree_avg(cur_root: NAryNode):
    if cur_root is None:
      return (0, 0)

    sumTot, numTot = 0, 0
    for child in cur_root.children:
      childNum, childSum = get_subtree_avg(child)
      sumTot += childSum
      numTot += childNum
    # calculate max 
    avg = (cur_root.val + sumTot) / (numTot + 1)
    
    if avg > maxAvg[0]:
      maxAvg = (cur_root, avg)
    
    return (numTot + 1, cur_root.val + sumTot)
  get_subtree_avg(root)
  return maxAvg[1]
    # update the root

  
    