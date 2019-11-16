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