class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        visited = [[0 for _ in range(n)] for _ in range(m)]

        u = [-1,0,1,0]
        v = [0,1,0,-1]

        def bfs(q):
            while q:
                i,j = q.popleft()
                for k in range(4):
                    a = i+u[k]
                    b = j+v[k]
                    if a >= 0 and a < m and b >= 0 and b < n:
                        if not visited[a][b] and grid[a][b] == "1":
                            visited[a][b] = 1
                            q.append((a,b))

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    visited[i][j] = 1 
                    if grid[i][j] == "1":
                        q = deque([(i,j)])
                        bfs(q)
                        ans += 1
        
        return ans
        
