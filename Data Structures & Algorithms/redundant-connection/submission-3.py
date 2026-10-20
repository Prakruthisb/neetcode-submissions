class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def detect_cycle(node,p):
            visited[node] = 1
            for nei in adj[node]:
                if visited[nei]:
                    if nei != p:
                        return True 
                    continue 
                if detect_cycle(nei,node):
                    return True 
            return False 
        
        adj = defaultdict(list)

        n = len(edges)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = [0]*(n+1)
            if detect_cycle(u,-1):
                return [u,v]