class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        a = 0
        b = len(plants) - 1
        refill = 0
        currA, currB = capacityA, capacityB
        while a < b:
            if currA < plants[a]:
                refill += 1
                currA = capacityA
            currA -= plants[a]
            a += 1
            
            if currB < plants[b]:
                refill += 1
                currB = capacityB
            currB -= plants[b]
            b -= 1
            
            if a == b and currA < plants[a] and currB < plants[a]:
                refill += 1
                
        return refill