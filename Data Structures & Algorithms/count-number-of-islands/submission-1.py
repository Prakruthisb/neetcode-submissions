class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        ans = 0

        def bfs(row,col):
            q = deque([(row,col)])
            while q:
                r,c = q.popleft()
                for i in range(4):
                    nr,nc = r+dr[i],c+dc[i]
                    if 0 <= nr <m and 0 <= nc <n and grid[nr][nc] == '1' and not visited[nr][nc]:
                        visited[nr][nc] = 1 
                        q.append((nr,nc))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i,j)
                    ans += 1 
        
        return ans 