class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = [[]]
        for num in nums:
            for i in range(len(power_set)):
                power_set.append(power_set[i] + [num])
        return power_set