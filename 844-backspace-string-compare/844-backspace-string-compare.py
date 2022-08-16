class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(st):
            stack = []
            for char in st:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
                    
                    
            return "".join(stack)
        return helper(s) == helper(t)