class Solution:
    def maximum69Number (self, num: int) -> int:
        x = list(str(num))
        
        for i, char in enumerate(x):
            if char == '6':
                x[i] = '9'
                break
                
        return "".join(x)