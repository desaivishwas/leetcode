from collections import defaultdict
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        res = []
        scores =  defaultdict(list)
        
        for score in items:
            scores[score[0]].append(score[1])
        for k, v in scores.items():
            v.sort(reverse=True)
            res.append([k , sum(v[:5]) // 5])
            res.sort()
            
        return res