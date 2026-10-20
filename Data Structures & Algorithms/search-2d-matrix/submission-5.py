class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(row,l,r):
            while l<=r:
                m = (l+r)//2
                if matrix[row][m] == target:
                    return True 
                elif matrix[row][m] < target:
                    l = m+1 
                else:
                    r = m-1 
            return False 
        
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n-1]:
                return bs(i,0,n-1)
        return False 