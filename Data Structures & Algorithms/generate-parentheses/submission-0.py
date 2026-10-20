class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def fun(op,cl,s):
            if op == cl == n:
                ans.append(s)
                return 
            if op < n:
                fun(op+1,cl,s+"(")
            if cl < n and cl < op:
                fun(op,cl+1,s+")")
        
        fun(0,0,"")
        return ans 