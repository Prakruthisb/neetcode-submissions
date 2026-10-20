class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])
        ans = []
        pac,alt = set(),set()

        row = [-1,0,1,0]
        col = [0,1,0,-1]        

        def dfs(r,c,visit,prevHeight):
            if ((r,c) in visit or 
                r<0 or c<0 or r>=m or c>=n or 
                heights[r][c] < prevHeight):
                return 
            visit.add((r,c))
            for i in range(4):
                nr,nc = r+row[i],c+col[i]
                dfs(nr,nc,visit,heights[r][c])
        
        for c in range(n):
            dfs(0,c,pac,heights[0][c])
            dfs(m-1,c,alt,heights[m-1][c])
        
        for r in range(m):
            dfs(r,0,pac,heights[r][0])
            dfs(r,n-1,alt,heights[r][n-1])
        
        for i in range(m):
            for j in range(n):
                if (i,j) in pac and (i,j) in alt:
                    ans.append([i,j])
        
        return ans 