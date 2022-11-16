class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(list)  
        for num in nums1:
            d[num].append(nums2.index(num))
            
        return [d[num].pop() for num in nums1]