class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        end = float('-inf')
        ans = 0
        n = len(intervals)
        for i in range(n):
            if intervals[i][0] < end:
                ans += 1 
            else:
                end = intervals[i][1]
        return ans