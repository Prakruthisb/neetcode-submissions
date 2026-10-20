class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False 
        
        n = len(hand) 
        d = {}

        for num in hand:
            d[num] = d.get(num,0)+1
        
        for _ in range(n//groupSize): 
            val = min(d)
            for i in range(groupSize):
                if not val in d:
                    return False 
                d[val] -= 1 
                if d[val] == 0:
                    del d[val]
                val = val + 1 
        
        return True 