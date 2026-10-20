class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        n = len(digits) 
        ans = []
        path = []

        d = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        def fun(ind):
            if ind>=n:
                ans.append("".join(path))
                return 
            for ch in d[digits[ind]]:
                path.append(ch)
                fun(ind+1)
                path.pop()
        
        fun(0)
        return ans 