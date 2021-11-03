class Solution:
    def validPalindrome(self, s: str) -> bool:
        # if a palindrome
        if s == s[::-1]:
            return True
        else:
            i, j = 0, len(s)-1
            while(i<j):
                if s[i] == s[j]:
                    i+=1
                    j-=1
                    continue
                else:
                    a = s[0:j]+s[j+1:]
                    b = s[0:i]+s[i+1:]
                    break
            return True if a == a[::-1] or b == b[::-1] else False
               
            