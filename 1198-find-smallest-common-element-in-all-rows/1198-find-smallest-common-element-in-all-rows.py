class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        d = {}
        
        for row in mat:
            for elem in row:
                d[elem] = 1 + d.get(elem, 0)
                
        for k,v in d.items():
            if v == len(mat):
                return k
            
        return -1