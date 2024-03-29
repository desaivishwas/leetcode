class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = [0]*(max(nums) + 1)
        
        for i in nums:
            d[i] += i
            
        p2, p1 = 0, 0
                
        for i in range(len(d)):
            p1, p2 = max(d[i]+p2, p1), p1
        
        return max(p1, p2)