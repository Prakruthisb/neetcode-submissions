class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_possible(num):
            cunt = 0
            for p in piles:
                if p%num == 0:
                    cunt += (p/num)
                else:
                    cunt += (p//num)+1
            if cunt <= h:
                return True 
            else:
                return False

        l,r = 1,max(piles)
        while l<=r:
            m = (l+r)//2
            if is_possible(m):
                r = m -1 
            else:
                l = m+1
        return l