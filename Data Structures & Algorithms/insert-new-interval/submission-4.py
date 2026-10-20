class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    
        arr = []
        n = len(intervals)
        newI = 0
        for i in range(n):
            if newInterval[0] <= intervals[i][0]:
                if newInterval[0] == intervals[i][0] and newInterval[1] > intervals[i][1]:
                    arr.append(intervals[i])
                else:
                    arr.append(newInterval)
                    newI = 1
                    arr.append(intervals[i])
            elif newInterval[0] > intervals[i][0]:
                arr.append(intervals[i])
        
        if not newI:
            arr.append(newInterval)

        n = len(arr)
        ans = []
        for i in range(n):
            if not ans or arr[i][0] > ans[-1][1]:
                ans.append(arr[i])
            elif arr[i][0] <= ans[-1][1]:
                start,end = ans.pop()
                ans.append([start,max(arr[i][1],end)])
        return ans