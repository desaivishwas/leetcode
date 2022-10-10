class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        ''' O(MN)  O(m * n)'''
        
        num_rows = len(matrix)
        num_cols = 0 if num_rows < 0 else len(matrix[0])
        # Add an extra all zero column and row outside of the actual dp table
        # to simplify the transition
        
        dp = [[0]*(num_cols+1) for _ in range(num_rows+1)]
         
        num_squares = 0
        
        for i in range(1, num_rows + 1):
            for j in range(1, num_cols + 1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1
                    num_squares += dp[i][j]
        return num_squares