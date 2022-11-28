class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = {}
        seen = set()
        for w, l in matches:
            seen.add(w)
            seen.add(l)
            d[l] = d.get(l, 0) + 1
            
        zero, one = [], []
        for player in seen:
            count = d.get(player, 0)
            if count == 0:
                zero.append(player)
            elif count == 1:
                one.append(player)
                
        return [sorted(zero), sorted(one)]
                
                
            