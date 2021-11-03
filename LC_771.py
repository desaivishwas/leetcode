class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        j = set(jewels)
        for x in j:
            if x in stones:
                count += stones.count(x)
                continue
        return count
            