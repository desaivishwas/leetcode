class Solution:
    def countBits(self, n: int) -> List[int]:
        def binary(n , res = ""):
            if n == 0:
                return (res)
            else:
                res += str(n % 2)
                n = n // 2
                return binary(n , res)
            
        res = []
        for i in range(n + 1):
            x = binary(i, "").count("1")
            res.append(x)
            
        return res
            
        