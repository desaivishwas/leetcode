class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        x = len(candyType) // 2
        y = len(set(candyType))
        
        return min(x, y)
        