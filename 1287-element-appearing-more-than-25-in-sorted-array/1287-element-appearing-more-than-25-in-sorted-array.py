class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = int(len(arr) * 0.25)
        d = {}
        for num in arr:
            d[num] = 1 + d.get(num, 0)
            
            
        for k,v in d.items():
            if v > n:
                return k