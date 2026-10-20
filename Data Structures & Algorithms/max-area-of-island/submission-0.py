class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0 
        m,n = len(grid),len(grid[0])
        visited = [[0 for _ in range(n)]for _ in range(m)]
        row = [-1,0,1,0]
        col = [0,1,0,-1]

        def dfs(r,c):
            nonlocal cunt 
            for i in range(4):
                nr,nc = r+row[i],c+col[i]
                if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    cunt += 1 
                    dfs(nr,nc)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    cunt = 1 
                    visited[i][j] = 1 
                    dfs(i,j)
                    ans = max(ans,cunt)

        return ans 
        