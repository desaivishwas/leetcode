class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        d = defaultdict(int)
        
        for i in arr1:
            d[i] += 1
        
        for j in arr2:
            res.extend([j] * d[j])
        
        for k in sorted(list(set(arr1) - set(arr2))):
            res.extend([k] * d[k])
        
        return res