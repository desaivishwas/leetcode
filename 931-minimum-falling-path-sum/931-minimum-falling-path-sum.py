class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[-1]*len(matrix) for i in range(len(matrix))]
        
        def solve(A, i, j):
            if i >= len(A) or j >= len(A) or j < 0:
                return float("inf")
            
            if i == len(A) - 1:
                return A[i][j]
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = A[i][j]+ min(solve(A,i+1,j),solve(A,i+1,j-1),solve(A,i+1,j+1))

            return dp[i][j]
        
        res = float("inf")
        for j in range(len(matrix)):
            res = min(res,solve(matrix,0,j))
        return res
        