class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid),len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        
        row = [-1,0,1,0]
        col = [0,1,0,-1]
        while q:
            r,c,d = q.popleft()
            for i in range(4):
                nr,nc = r+row[i],c+col[i]
                if nr>=0 and nr<m and nc>=0 and nc<n:
                    if (d+1)<grid[nr][nc]:
                        grid[nr][nc] = d+1
                        q.append((nr,nc,d+1))