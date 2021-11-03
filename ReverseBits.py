class Solution:
    def reverseBits(self, n: int) -> int:
        index = 0
        for i in range(32):
            index = (index << 1) + (n & 1)
            n >>= 1
        return index