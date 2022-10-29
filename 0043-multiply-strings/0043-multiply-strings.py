class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def strToInt(num):
            mul = 1
            res = 0
            for n in reversed(num):
                res += mul * (ord(n) - ord('0'))
                mul *= 10
            return res
                      
        return str(strToInt(num1) * strToInt(num2))