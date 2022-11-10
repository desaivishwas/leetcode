class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        stack = []
        
        a = s[0]
        
        for i in s:
            if len(stack) == 0:
                res += 1
                a = i
            
            if i == a:
                stack.append(i)
            elif len(stack) != 0:
                stack.pop()
                
        return res
                