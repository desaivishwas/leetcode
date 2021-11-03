class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # length = 0
        n = len(s)
        sol = 0
        
        index= {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in index:
                i = max(index[s[j]], i)

            sol = max(sol, j - i + 1)
            index[s[j]] = j + 1

        return sol