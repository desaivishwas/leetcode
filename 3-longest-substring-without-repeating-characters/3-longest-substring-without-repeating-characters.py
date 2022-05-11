class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n), O(n)
        # to check duplicates
        charSet = set()
        # sliding window pointer 1
        left = 0
        res = 0    
        # iterating through the array
        for right in range(len(s)):
            while s[right] in charSet:
                # if char in set, remove from set, incremant left and shorten window size
                charSet.remove(s[left])
                left += 1
            # adding char to set
            charSet.add(s[right])
            # calc lenght of substring
            res = max(res, right - left + 1)
            
        return res