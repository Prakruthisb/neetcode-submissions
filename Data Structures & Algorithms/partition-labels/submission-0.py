class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        n = len(s)

        d = {}
        for i in range(n-1,-1,-1):
            if s[i] not in d:
                d[s[i]] = i 

        st = 0 
        ind = d[s[0]]

        for i in range(n):
            if ind == i:
                ans.append(i-st+1)
                st = i + 1 
                if st<n:
                    ind = d[s[st]] 
            elif d[s[i]] > ind:
                ind = d[s[i]]
        
        return ans 