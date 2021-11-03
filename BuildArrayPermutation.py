from typing import List
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # return nums
        n =  len(nums)
        ans = [] * (n-1)
        # print(ans)
        for num in nums:
            ans.append(nums[num])
        return ans
        
        