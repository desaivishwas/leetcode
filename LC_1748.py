class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum = 0
        res = []
        # numSet = set(nums)
        # print(numSet)
        counter = Counter(nums)
        # print(counter)
        for i, j in counter.items():
            if j==1:
                res.append(i)
        
        for ele in res:
            sum += ele
        return sum