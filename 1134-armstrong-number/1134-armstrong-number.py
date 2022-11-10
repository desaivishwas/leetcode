class Solution:
    def isArmstrong(self, n: int) -> bool:
        nums = list(str(n))
        res = 0
        k = len(nums)
        for num in nums:
            res += (int(num) ** k)
        return res == n