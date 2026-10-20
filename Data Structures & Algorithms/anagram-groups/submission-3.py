class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def validAnagrams(s,t):
            if len(s) != len(t):
                return False 
            a = [0]*26
            for i in range(len(s)):
                a[ord(s[i])-ord('a')] += 1
                a[ord(t[i])-ord('a')] -= 1 
            
            for val in a:
                if val != 0:
                    return False
            return True

        ans = []
        n = len(strs)
        visited = [0]*n

        for i in range(n):
            if visited[i]:
                continue 
            visited[i] = 1 
            cur = [strs[i]]
            for j in range(i+1,n):
                if not visited[j] and validAnagrams(strs[i],strs[j]):
                    visited[j] = 1 
                    cur.append(strs[j]) 
            ans.append(cur)
        
        return ans