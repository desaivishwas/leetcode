class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix) == 1:
            return True
        
        for i in range(len(matrix) - 1):
            row1, row2 = matrix[i], matrix[i + 1]
            for j in range(len(matrix[0]) - 1):
                if row1[j] != row2[j + 1]:
                    return False
        return True
        