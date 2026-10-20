class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False 


        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [0]*n
        def detect_cycle(node,p):
            visited[node] = 1 
            for nei in adj[node]:
                if visited[nei] and nei != p:
                    return True 
                if visited[nei]:
                    continue 
                if detect_cycle(nei,node):
                    return True 
        
        cunt = 0
        for i in range(n):
            if not visited[i]:
                cunt += 1 
                if cunt > 1:
                    return False 
                if detect_cycle(0,-1):
                    return False 
        return True 
                