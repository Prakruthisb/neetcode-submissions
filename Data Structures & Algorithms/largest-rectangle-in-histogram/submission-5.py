class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0 

        s = [(-1,-1)]
        for i,val in enumerate(heights):
            while val < s[-1][0]:
                top_val,top_ind = s.pop()
                area = ((i-s[-1][1])-1)*top_val
                ans = max(ans,area)
            s.append((val,i))

        while s[-1] != (-1,-1):
            rm = n 
            top_val,top_ind = s.pop()
            lm = s[-1][1]
            area = ((rm-lm)-1)*top_val
            ans = max(ans,area)
        
        return ans 