from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 2nd pointer
        j = len(s) - 1
        for i in range(len(s)):
            s[i], s[j] =s[j],s[i]
            j-=1
            i+=1
            if j == i or j < i:
                break
        return s
        