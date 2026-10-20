class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(row,low,h):
            while low<=h:
                c = (low+h)//2
                if matrix[row][c] == target:
                    return True 
                elif matrix[row][c] < target:
                    low = c+1 
                else:
                    h = c-1
            return False

        m = len(matrix)
        n = len(matrix[0])

        l,r = 0,m-1
        while l<=r:
            mid = (l+r)//2
            if target >= matrix[mid][0] and target <= matrix[mid][n-1]:
                return bs(mid,0,n-1)
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1 
        return False