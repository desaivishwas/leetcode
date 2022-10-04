class Solution:
    def tribonacci(self, n: int) -> int:
        res = [0,1,1]
        i = 0
        while i <= n:
            res.append(res[i] + res[i+1]+ res[i+2])
            i += 1
            
        return res[n]