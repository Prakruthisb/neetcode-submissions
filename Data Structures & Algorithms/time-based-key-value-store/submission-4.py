class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.d:
            return ""
        self.d[key].sort(key=lambda x:x[1],reverse=True)
        for val,time in self.d[key]:
            if time <= timestamp:
                return val 
        return ""