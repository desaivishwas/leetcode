class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]  * n for _ in range(m)]
        for c in range(1, m):
            for r in range(1, n):
                dp[c][r] = dp[c - 1][r] + dp[c][r - 1]
        return dp[m-1][n-1]
        
        
         # return math.comb(m + n - 2, n - 1)
        