class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        # print(count)
        for key, value in enumerate(s):
            if count[value] == 1:
                return key
        return -1