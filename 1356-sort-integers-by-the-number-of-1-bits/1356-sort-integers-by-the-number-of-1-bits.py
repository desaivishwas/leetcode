class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def helper(n, res = ""):
            if n == 0:
                return (res)
            else:
                res += str(n % 2)
                n = n // 2
                return helper(n, res)
            
        res = []
        arr.sort()
        for num in arr:
            res.append((num, helper(num, "").count("1")))
            
        res.sort(key = lambda x:x[1])
        
        return [k for (k,val) in res]
            
        
        