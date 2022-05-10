class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        nums = sorted(list(set(nums)))
        earn1, earn2 = 0, 0
        
        # dp = [0 for _ in range(len(nums))]
        # dp[0] = nums[0]
        
        for i in range(len(nums)):
            curr = nums[i] * count[nums[i]]
            # when we cannot use curr and earn 2
            if i > 0 and nums[i] == nums[i-1] + 1:
                temp = earn2
                earn2 = max(curr + earn1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = curr + earn2
                earn1 = temp
                
        return earn2