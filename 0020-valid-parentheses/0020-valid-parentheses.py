class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(','}':'{', ']':'['}
        stack = []
        for char in s:
            if char in d:
                top = stack.pop() if stack else "#"
                
                if d[char] != top:
                    return False
            else:
                stack.append(char)
                
        return len(stack) == 0