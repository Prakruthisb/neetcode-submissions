class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = -1
        n = len(heights)
        for i in range(n):
            for j in range(i+1,n):
                width = j-i
                max_water = width * min(heights[i],heights[j])
                ans = max(ans,max_water)
        return ans