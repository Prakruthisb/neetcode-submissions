class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for u,v in prerequisites:
            adj_list[v].append(u)
        
        path = [0]*numCourses
        visited = [0]*numCourses

        def detect_cycle(node):
            if path[node]:
                return True
            if visited[node]:
                return False
            else:
                visited[node] = 1
                path[node] = 1
                if adj_list[node]:
                    for nei in adj_list[node]:
                        if detect_cycle(nei):
                            return True
                path[node] = 0
                return False

        
        for i in range(numCourses):
            if not visited[i]:
                if detect_cycle(i):
                    return False 
        return True
