class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ans = []
        i = 0
        while i < n:
            if newInterval[0] <= intervals[i][1]:
                break 
            i+=1
        ans = ans + intervals[0:i]

        left,right = newInterval[0],newInterval[1]
        while i<n:
            if intervals[i][0] <= newInterval[1]:
                left = min(left,intervals[i][0])
                right = max(right,intervals[i][1])
                i += 1 
            else:
                break
        ans.append([left,right])
        ans = ans + intervals[i:]
        return ans