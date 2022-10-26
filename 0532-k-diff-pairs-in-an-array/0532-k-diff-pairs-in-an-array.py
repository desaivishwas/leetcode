class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        d = {}
        
        for num in nums:
            d[num] = 1 + d.get(num, 0)
            
        for x in d:
            if k > 0 and  x + k in d:
                res += 1
            elif k == 0 and d[x] > 1:
                res += 1
                
        return res