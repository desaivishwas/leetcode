class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while True:
            n = sum(int(c) ** 2 for c in str(n))
            if n == 1:
                return True

            if n in nums:
                return False
            nums.add(n)
            