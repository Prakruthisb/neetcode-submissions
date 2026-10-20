class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        i,j = 0,n-1
        lm = 0 
        rm = 0 
        
        while i<j:
            if height[i]<=height[j]:
                if height[i] >= lm:
                    lm = height[i]
                else:
                    ans += (lm-height[i])
                i+=1 
            else:
                if height[j] >= rm:
                    rm = height[j]
                else:
                    ans += (rm-height[j])
                j-=1
        return ans