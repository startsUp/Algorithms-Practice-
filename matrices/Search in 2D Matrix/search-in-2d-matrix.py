def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        bT = False
        while (i < m and j < n and i >= 0 and j >= 0):
            if (matrix[i][j] == target): return True # if found return
            if (matrix[i][j] < target): 
                # if backtracking and we find an element < target, or on last row, go right
                if (bT or i == m - 1): j+=1 
                else: i+=1 # go bottom
            else: i-=1; bT=True 
            # if current element is greater than target, we gotta backtrack to explore right elements 
            
        return False