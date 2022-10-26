class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        maxi = 0
        for j in range(len(s)):
            for i in range(j+1):
                dp[i][j] = ((s[i] == s[j]) and ((j - i <= 2) or dp[i+1][j-1]))
                if dp[i][j]:
                    if (j - i + 1) > maxi:
                        maxi = j - i + 1
                        
                        res = s[i:j+1]
                        
        return res