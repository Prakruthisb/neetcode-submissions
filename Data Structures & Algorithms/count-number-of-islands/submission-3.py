class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        ans = 0

        def dfs(row,col):
            for i in range(4):
                nr,nc = row+dr[i],col+dc[i]
                if 0 <= nr <m and 0 <= nc <n and grid[nr][nc] == '1' and not visited[nr][nc]:
                    visited[nr][nc] = 1 
                    dfs(nr,nc)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    visited[i][j] = 1
                    dfs(i,j)
                    ans += 1 
        
        return ans 