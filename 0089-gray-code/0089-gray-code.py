class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for num in range(1, 2**n):
            b = bin(num).replace('0b', '')
            s = b[0]
            for i in range(1,len(b)):
                x = int(b[i-1]) ^ int(b[i])
                x = str(x)
                s += x
                
            res.append(int(s, 2))
            
            
        return res