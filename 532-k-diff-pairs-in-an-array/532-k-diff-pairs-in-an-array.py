from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        count = Counter(nums)
        
        for c in count:
            if k > 0 and c + k in count:
                res += 1
            elif k == 0 and count[c] > 1:
                res += 1
        return res
            
        
        
        
        
        # O(nlogn)
#         s = []
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] - nums[i-1] == k:
#                 s.append((nums[i], nums[i-1]))
                
        
#         return len(s)
            
            
        