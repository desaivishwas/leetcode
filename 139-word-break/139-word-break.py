class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict) #O(M)
        dp = [True] + [False] * len(s)
        for i in range(len(s)): # O(N)
            if dp[i]:
                for j in range(i + 1, len(s) + 1): # O(N)
                    if s[i:j] in wordSet: # O(N) String Generation
                        dp[j] = True     
        return dp[-1]
        
        
        
        
        # d = [False] * len(s)    
        # for i in range(len(s)):
        #     for w in wordDict:
        #         if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
        #             d[i] = True
        # return d[-1]
        