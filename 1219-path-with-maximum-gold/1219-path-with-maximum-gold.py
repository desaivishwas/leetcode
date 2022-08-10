class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # Time: O(MN)
        # Space: O(MN)
        row, col = len(grid), len(grid[0])
        
        
        def dfs(i,j):
            currGold  = grid[i][j]
            grid[i][j] = 0
            goldFound = 0
            for x,y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < row and 0 <= y < col and grid[x][y] != 0:
                    goldFound = max(goldFound, dfs(x,y))
            grid[i][j] = currGold
            
            return goldFound + currGold
        
        
        
        goldFound = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] != 0:
                    goldFound = max(goldFound, dfs(r, c))
                
        return goldFound
    
    
        
            
    