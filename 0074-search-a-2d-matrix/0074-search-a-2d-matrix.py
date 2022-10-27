class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(row):
            left, right = 0, len(matrix[0]) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            return False
        
        for r in range(len(matrix)):
            if matrix[r][0] <= target and matrix[r][len(matrix[0]) - 1] >= target:
                return binarySearch(r)
            
        return False