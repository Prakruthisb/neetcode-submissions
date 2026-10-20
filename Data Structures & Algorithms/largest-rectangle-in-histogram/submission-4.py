class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h = [(-1, -1)]          # (height, index)
        n = len(heights)
        ans = 0

        for i in range(n):
            while heights[i] < h[-1][0]:
                height, ind = h.pop()
                right = i
                left = h[-1][1]          # Previous smaller element
                area = (right - left - 1) * height
                ans = max(ans, area)

            h.append((heights[i], i))

        while h[-1] != (-1, -1):
            height, ind = h.pop()
            right = n
            left = h[-1][1]              # Previous smaller element
            area = (right - left - 1) * height
            ans = max(ans, area)

        return ans