class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def isanagrams(str1,str2):
            if len(str1) != len(str2):
                return False 

            a = [0]*26

            for i in range(len(str1)):
                a[ord(str1[i])-ord('a')] += 1 
                a[ord(str2[i])-ord('a')] -= 1 

            for val in a:
                if val != 0:
                    return False 
            return True

        ans = []
        n = len(strs)
        anagram = [0]*n

        for i in range(n):
            temp = []
            if anagram[i] == 0:
                anagram[i] = 1
                temp.append(strs[i]) 
                for j in range(i+1,n):
                    if isanagrams(strs[i],strs[j]):
                        temp.append(strs[j])
                        anagram[j] = 1
                ans.append(temp)
        return ans