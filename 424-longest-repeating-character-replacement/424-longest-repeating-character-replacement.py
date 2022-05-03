class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Note: 
        O(n)
        hash map to count occurences
        windowLne-  count gives the no of char to replace
        
        '''
        d = {}
        res = 0
        left = 0
        for right in range(len(s)) :
            # hash map to count occurences
            d[s[right]] = 1 + d.get(s[right], 0)
               
            if (right -left + 1) - max(d.values()) > k:
                d[s[left]] -= 1
                left += 1
                
                
            res = max(res, right - left + 1)

        return res
        
        