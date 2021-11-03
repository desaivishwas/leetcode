from typing import Collection, List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Collection. Counter(nums)
        for key, (ele,counts) in enumerate(count.items()):
            # print(key)
            if counts ==  1:
                return ele
    
        """ Much faster"""    
#         hash_table = defaultdict(int)
#         for i in nums:
#             hash_table[i] += 1        
#         for i in hash_table:
#             if hash_table[i] == 1:
#                 return i 
            
 