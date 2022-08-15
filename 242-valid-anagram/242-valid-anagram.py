class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dict have iverheads hence array since the data is smaller
        # hash tavles take extra space
        # codepath 06/07
        
        # Time: O(n)
        # Space: O(1)
        
        
        if len(s) != len(t):
            return False
            
        char_counts = [0] * 26
        
        for i in range(len(s)):
            char_counts[ord(s[i]) - ord('a')] += 1
            char_counts[ord(t[i]) - ord('a')] -= 1
         
        
        # return sum(char_counts) == 0
        for value in char_counts:
            if value != 0:
                return False
        return True
        