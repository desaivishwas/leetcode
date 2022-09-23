class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ''' Ciount the oddd factors to get the sol'''
        
        count = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if  n % i == 0:
                if i % 2:
                    count += 1
                    
                if (n/i) % 2 and n/i != i:
                    count += 1
                    
                    
        return count
        
        
#         count, k = 0, 1
#         while 2 * n > k * (k-1):
#             numerator = n - (k * (k-1) // 2)
#             if numerator % k == 0:
#                 count += 1
            
#             k += 1
#         return count 
        