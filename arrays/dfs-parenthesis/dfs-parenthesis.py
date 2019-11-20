class Solution:
    def generateParenthesis(self, n: int):
        res = []
        self.dfs(n, n, n,'', res)
        return res
    
    def dfs(self, n, current, last, path, res):
        if current == 0:
            res.append(path)
        else:
            for i in range(n):
                if(last == i or i == current):
                    continue
                else:
                    self.dfs(n, i, current, current*'(' + path + ')'*current, res)


x = Solution()
print(x.generateParenthesis(3))
