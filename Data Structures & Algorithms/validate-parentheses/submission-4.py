class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(',']':'[','}':'{'}
        stack = []
        
        for ch in s:
            if ch in d.values():
                stack.append(ch)
            elif not stack or d[ch] != stack[-1]:
                return False 
            else:
                stack.pop()
        if not stack:
            return True 
        else:
            return False