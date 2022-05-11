class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n), Space: O(n)
        # to check duplicates
        charSet = set()
        # sliding window pointer 1
        left, res = 0, 0    
        # iterating through the array
        for right in range(len(s)):
            while s[right] in charSet:
                # if char in set, remove from set, increment left and shorten window size
                charSet.remove(s[left])
                left += 1
            # adding char to set
            charSet.add(s[right])
            # calc length of substring
            res = max(res, right - left + 1)
            
        return res