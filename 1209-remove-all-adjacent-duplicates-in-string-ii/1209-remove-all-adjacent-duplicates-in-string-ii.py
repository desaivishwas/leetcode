class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack, counter = [], []
        for char in s:
            if not stack or stack[-1] != char:
                stack.append(char)
                counter.append(1)
            elif stack[-1] == char:
                counter[-1] += 1
                
            if counter[-1] == k:
                counter.pop()
                stack.pop()
                
        return ''.join([stack[i] * counter[i] for i in range(len(stack))])
    
    