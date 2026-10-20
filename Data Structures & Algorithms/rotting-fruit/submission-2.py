class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        ans = 0

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j,0))
        
        row = [-1,0,1,0]
        col = [0,1,0,-1]
        while q:
            r,c,time = q.popleft()
            ans = max(ans,time)
            for i in range(4):
                nr,nc = r+row[i],c+col[i]
                if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                        q.append((nr,nc,time+1))
                        grid[nr][nc] = 2 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1 
        return ans
        