class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lol = [[1]]
        for i in range(1, rowIndex + 1):
            temp = [1 for _ in range(i+1)]
            for j in range(1, len(temp)-1):
                temp[j] = lol[-1][j] + lol[-1][j-1]
                
            lol.append(temp)
            
        return lol[-1]