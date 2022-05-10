class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count, k = 0, 1
        while 2 * n > k * (k-1):
            numerator = n - (k * (k-1) // 2)
            if numerator % k == 0:
                count += 1
            
            k += 1
        return count 
        