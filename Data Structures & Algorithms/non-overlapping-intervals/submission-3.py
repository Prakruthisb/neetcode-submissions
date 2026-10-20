class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        n = len(intervals)
        ans = 0
        prev = float('-inf')

        for i in range(n):
            if intervals[i][0] < prev:
                ans += 1 
            else:
                prev = intervals[i][1]
        return ans 