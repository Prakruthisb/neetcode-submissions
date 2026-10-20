class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h = []
        h.append((-1,-1))
        n = len(heights)
        ans = 0
        for i in range(n):
            while heights[i] < h[-1][0]:
                height,ind = h.pop()
                right = i
                left = -1
                for j in range(len(h)-1,-1,-1):
                    if h[j][0] < height:
                        left = h[j][1]
                        break
                area = (right - left -1) * height
                ans = max(area,ans)
            h.append((heights[i],i)) 
        while h:
            height,ind = h.pop()
            right = n
            left = -1
            for j in range(len(h)-1,-1,-1):
                if h[j][0] < height:
                    left = h[j][1]
                    break
            area = (right - left -1) * height
            ans = max(area,ans)
        return ans