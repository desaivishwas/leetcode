class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        res = 0
        flag = True
        
        for i in range(len(damage)):
            if damage[i] > armor and flag:
                res += damage[i] - armor
                flag = False
                
            else:
                res += damage[i]
                
        if flag:
            m = max(damage)
            res -= m
            
        return res + 1