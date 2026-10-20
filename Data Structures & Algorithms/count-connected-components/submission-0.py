class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        visited = [0]*n
        ans = 0

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            visited[node] = 1 
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                ans += 1 
        
        return ans