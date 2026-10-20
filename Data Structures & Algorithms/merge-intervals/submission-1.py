class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        ans = []
        for i in range(n):
            if not ans or intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            elif intervals[i][0] <= ans[-1][1]:
                start,end = ans.pop()
                ans.append([start,max(intervals[i][1],end)])
        return ans