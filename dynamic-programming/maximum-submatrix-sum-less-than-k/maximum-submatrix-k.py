class Solution:
  def precomputeSum(self, matrix):
    if len(matrix) == 0 or len(matrix[0])==0: 
            return 
    self.dp = [[0 for i in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)]
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            self.dp[r + 1][c + 1] = self.dp[r + 1][c] + self.dp[r][c + 1] + matrix[r][c] - self.dp[r][c]
  def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]
    
  def isSubMatrixSmaller(self, matrix, k, givenSum):
    r1, r2 = 0, k-1
    while (r2 < len(matrix)):
      c1, c2 = 0, k-1
      while (c2 < len(matrix[0])):
        if (self.sumRegion(r1, c1, r2, c2) > givenSum):
          return False
        c1, c2 = c1+1, c2+1
      r1, r2 = r1+1, r2+1
    return True
  def maximumSubmatrix(self, matrix, givenSum):
    # the key is to precompute the sums so getting submatrix sum is O(1) time. 
    self.precomputeSum(matrix)
    # assuming matrix is square 
    k = len(matrix)
    while (True):
      if(self.isSubMatrixSmaller(matrix, k, givenSum)):
        break
      k-=1 
    return k


test = Solution()
matrix = [[2,2,2], [3,3,3], [4,4,4]]
gS = 3
print("Max Submatrix size for sum", gS, " is ",  test.maximumSubmatrix(matrix, gS))


    # O
    #     A .. B
    #  .    .
    #     C .. D
    # Sum(ABCD) = SUM(OD) + SUM(OA) - (SUM(OC) + SUM(OB)) 
