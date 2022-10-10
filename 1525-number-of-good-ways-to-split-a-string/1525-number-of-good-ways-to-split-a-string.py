# from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        def get_distinct(count):
            c = 0
            for i in count:
                if i != 0:
                    c += 1
                    
            return c
        
        splits = 0
        left = [0] * 26
        right = [0] * 26
        
        for i in range(len(s)):
            right[ord(s[i]) - ord('a')] += 1
            
        for i in range(len(s)):
            left[ord(s[i]) - ord('a')] += 1
            right[ord(s[i]) - ord('a')] -= 1
        
            distinct_left = get_distinct(left)
            distinct_right = get_distinct(right)

            if distinct_left == distinct_right:
                splits += 1
                
                
        return splits
            