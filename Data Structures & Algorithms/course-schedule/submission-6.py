class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)
        
        visited = [0]*numCourses
        path_visited = [0]*numCourses
        
        def detect_cycle(node):
            if path_visited[node]:
                return True
            if visited[node]:
                return False
            visited[node] = 1 
            path_visited[node] = 1
            for nei in adj[node]:
                if detect_cycle(nei):
                    return True 
            path_visited[node] = 0 
            return False 

        for i in range(numCourses):
            if not visited[i]:
                if detect_cycle(i):
                    return False 
        return True 