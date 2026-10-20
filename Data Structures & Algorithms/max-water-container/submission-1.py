class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = -1
        n = len(heights)
        i,j = 0,n-1
        while i<j:
            ans = max(ans,(j-i) * min(heights[i],heights[j]))
            if heights[i] < heights[j]:
                i += 1 
            else:
                j -= 1 
        return ans