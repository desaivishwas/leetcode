class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle =  []
        for i in range(n):
            circle.append(i + 1)
        
        if k == 1 or n == 1:
            return circle[-1]
        idx = 0
        while len(circle) != 1:
            if idx > len(circle) - 1:
                idx = 0
            for _ in range(k - 1):
                idx += 1
                if idx > len(circle) - 1:
                    idx  = 0
            circle.pop(idx)
            
        return circle[0]