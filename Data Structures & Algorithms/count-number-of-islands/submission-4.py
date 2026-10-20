class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        ans = 0

        def dfs(row,col):
            for i in range(4):
                nr,nc = row+dr[i],col+dc[i]
                if 0 <= nr <m and 0 <= nc <n and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    dfs(nr,nc)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    dfs(i,j)
                    ans += 1 
        
        return ans 