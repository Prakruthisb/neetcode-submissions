class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        tal_left = [0]*n
        max_left = height[0]
        for i in range(1,n):
            tal_left[i] = max_left
            max_left = max(max_left,height[i])

        tal_right = [0]*n
        max_right = height[n-1]
        for i in range(n-2,-1,-1):
            tal_right[i] = max_right
            max_right = max(max_right,height[i])
        
        ans = 0
        for i in range(n):
            area = min(tal_left[i],tal_right[i]) - height[i]
            if area > 0:
                ans += area

        return ans