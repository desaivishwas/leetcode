class Solution:
    def numTeams(self, rating: List[int]) -> int:
        upper = [0] * len(rating)
        lower = [0] * len(rating)
        
        count  = 0
        for i in range(len(rating)):
            for j in range(i):
                if rating[i] > rating[j]:
                    count += upper[j]
                    upper[i] += 1
                    
                else:
                    count += lower[j]
                    lower[i] += 1
                    
        return count