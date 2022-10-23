class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        
        for i, marks in items:
            d[i].append(marks)
            
        res = []
        for k, v in d.items():
            v.sort(reverse = True)
        for k, v in d.items():
            res.append([k, sum(v[:5])//5])
        res = sorted(res, key = lambda x:x[0])
        return res
        