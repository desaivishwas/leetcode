class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m , n = len(grid) , len(grid[0])
        pos = list(range(n))
        
        for row in range(m):
            for col in range(n):
                if pos[col] > -1:
                    if grid[row][pos[col]] == -1:
                        if pos[col] == 0 or grid[row][pos[col] - 1] == 1:
                            pos[col] = -1
                        else:
                            pos[col] -= 1
                    
                    else:
                        if pos[col] == n - 1 or grid[row][pos[col] + 1] == -1:
                            pos[col] = -1
                        else:
                            pos[col] += 1
                            
        return pos