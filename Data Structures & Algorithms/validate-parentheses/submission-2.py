class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        d = {'(':')','[':']','{':'}'}
        for ch in s:
            if ch in d.keys():
                arr.append(ch)
            else:
                if not arr or ch != d[arr.pop()]:
                    return False 
        if arr:
            return False
        return True 
