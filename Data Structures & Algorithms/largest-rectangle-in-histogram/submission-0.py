class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)

        for i in range(n):
            height = heights[i]
            for j in range(i,n):
                height = min(height,heights[j])
                area = (j-i+1) * height
                ans = max(ans,area)
        return ans