from typing import List
from Collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count = Counter(nums1)
        nums2_count = Counter(nums2)
        res = nums1_count & nums2_count
        return list(res.elements())
        # res = []
        # for i in range(len(nums1)):
        #     for num in nums2:
        #         if num in nums1:
        #             res.append(num)
        # return res
                