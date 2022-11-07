class Solution:
    def toHex(self, num: int) -> str:
        hexed = "0123456789abcdef"
        result = []
        
        # if zero
        if not num:
            return "0"
        
        # if negative (two's compliment)
        num = num + 2**32 if num < 0 else num
        
        # make the digits
        while num:
            num, res = divmod(num, 16)
            result.append(hexed[res])
        
        return "".join(reversed(result))