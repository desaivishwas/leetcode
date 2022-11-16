class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(list)  
        for i, num in enumerate(nums2):
            d[num].append(i)
            
        return [d[num].pop() for num in nums1]