class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        ans = float('inf')
        wordList = set(wordList)

        alpha = "abcdefghijklmnopqrstuvwxyz"

        if endWord not in wordList:
            return 0 
        
        q = deque([(beginWord,1)])

        while q:
            word,cunt = q.popleft()
            if word == endWord:
                ans = min(ans,cunt)
            for i in range(n):
                for j in range(26):
                    if word[i] == alpha[j]:
                        continue 
                    nw = word[:i] + alpha[j] + word[i+1:]
                    if nw in wordList:
                        wordList.remove(nw)
                        q.append((nw,cunt+1))

        return 0 if ans == float('inf') else ans 