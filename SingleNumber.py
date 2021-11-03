from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = []
        for i in nums:
            if i not in count:
                count.append(i)
            else:
                count.remove(i)
        return count.pop()


# # driver code
#     nums1 = [4,1,2,1,2]
#     singleNumber(self,nums1)