class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.valStack = []
        self.count = 0
        self.dfs(root, sum)
        return self.count
    
    def dfs(self, root: TreeNode, sum: int):
        if(root is None):
            return
        for i in range(len(self.valStack)):
            self.valStack[i] = self.valStack[i] - root.val
            if(self.valStack[i] == 0):
                self.count+=1
        if(sum-root.val == 0):
            self.count+=1
        self.valStack.append(sum-root.val)
        self.dfs(root.left, sum)
        self.dfs(root.right, sum)
        self.valStack.pop()
        for i in range(len(self.valStack)):
            self.valStack[i]+=root.val
