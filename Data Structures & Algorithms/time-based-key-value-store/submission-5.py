class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.d:
            return ""
        n = len(self.d[key])
        res = ""
        l,r = 0 , n-1
        while l<=r:
            m = (l+r)//2
            if self.d[key][m][1] <= timestamp:
                res = self.d[key][m][0]
                l = m+1
            else:
                r = m-1 
        return res