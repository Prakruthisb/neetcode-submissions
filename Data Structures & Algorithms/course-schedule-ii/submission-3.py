class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)

        visited = [0]*numCourses
        path_visited = [0]*numCourses
        ans = []

        def detect_cycle(node):
            visited[node] = 1 
            path_visited[node] = 1 
            for nei in adj[node]:
                if visited[nei] and path_visited[nei]:
                    return True 
                if visited[nei]:
                    continue 
                if detect_cycle(nei):
                    return True 
            path_visited[node] = 0 
            ans.append(node)
        
        for i in range(numCourses):
            if not visited[i]:
                if detect_cycle(i):
                    return []

        return ans[::-1]