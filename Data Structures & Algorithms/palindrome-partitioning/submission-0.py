class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s) 
        ans = [] 

        def is_palindrome(string):
            i,j = 0,len(string)-1
            while i<j:
                if string[i] != string[j]:
                    return False 
                i += 1 
                j -= 1 
            return True

        def fun(ind,arr):
            if ind >= n:
                ans.append(arr.copy())
                return 
            
            for i in range(ind,n):
                string = s[ind:i+1]
                if is_palindrome(string):
                    arr.append(string)
                    fun(i+1,arr)
                    arr.pop()
        
        fun(0,[])
        return ans