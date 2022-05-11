class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        new = list(range(1, n+1))
        while len(new) > 1:
            i = (k-1) % len(new)
            new = new[i+1:] + new[:i]

        return new[0]