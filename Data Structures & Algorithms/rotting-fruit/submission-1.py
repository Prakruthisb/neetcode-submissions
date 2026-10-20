class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        visited = [[0 for _ in range(n)]for _ in range(m)]
        ans = 0

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                    visited[i][j] = 1 
        
        row = [-1,0,1,0]
        col = [0,1,0,-1]
        while q:
            r,c,time = q.popleft()
            for i in range(4):
                nr,nc = r+row[i],c+col[i]
                if nr>=0 and nr<m and nc>=0 and nc<n and not visited[nr][nc]:
                    visited[nr][nc] = 1 
                    if grid[nr][nc] == 1:
                        q.append((nr,nc,time+1))
                        ans = max(ans,time+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    return -1 
        return ans
        