class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        row = [-1,0,1,0]
        col = [0,1,0,-1]

        def dfs(r,c,ind):
            if ind >= len(word):
                return True 
            visited[r][c] = 1 
            for i in range(4):
                nr,nc = r + row[i],c + col[i]
                if 0<=nr<m and 0<=nc<n and not visited[nr][nc] and board[nr][nc] == word[ind]:
                    if dfs(nr,nc,ind+1):
                        return True
            visited[r][c] = 0 

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j,1):
                        return True 
        return False