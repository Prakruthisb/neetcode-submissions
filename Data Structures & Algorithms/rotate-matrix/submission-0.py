class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix) #rows 
        n = len(matrix[0]) #cols
        temp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                temp[j][n-1-i] = matrix[i][j]
        
        for i in range(m):
            for j in range(n):
                matrix[i][j] = temp[i][j]