class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board),len(board[0])
        visited = [[0 for _ in range(n)]for _ in range(m)]

        row = [-1,0,1,0]
        col = [0,1,0,-1]
        def dfs(r,c):
            visited[r][c] = 1 
            for i in range(4):
                nr,nc = r+row[i],c+col[i]
                if nr>=0 and nr<m and nc>=0 and nc<n and not visited[nr][nc] and board[nr][nc] == 'O':
                    dfs(nr,nc)

        for i in range(n):
            if board[0][i] == 'O' and not visited[0][i]:
                dfs(0,i)
            if board[m-1][i] == 'O' and not visited[m-1][i]:
                dfs(m-1,i)
        
        for i in range(m):
            if board[i][0] == 'O' and not visited[i][0]:
                dfs(i,0)
            if board[i][n-1] == 'O' and not visited[i][n-1]:
                dfs(i,n-1)
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and board[i][j] == 'O':
                    board[i][j] = 'X'