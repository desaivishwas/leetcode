class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * r for r in range(1, numRows + 1)]
        for row in range(2, numRows):
            for i in range(1, row):
                res[row][i] = res[row - 1][i - 1] + res[row - 1][i]
                
        return res