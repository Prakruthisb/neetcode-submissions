class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0 
        m,n = len(grid),len(grid[0])
        row = [-1,0,1,0]
        col = [0,1,0,-1]

        def dfs(r,c):
            nonlocal cunt 
            for i in range(4):
                nr,nc = r+row[i],c+col[i]
                if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    cunt += 1 
                    dfs(nr,nc)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cunt = 1 
                    grid[i][j] = 0
                    dfs(i,j)
                    ans = max(ans,cunt)

        return ans 
        