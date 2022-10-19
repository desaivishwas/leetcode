class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
                
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = a + nums[left] + nums[right]
                    
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                    
                else:
                    res.append([a, nums[left], nums[right]])
                    # increment left and right pointers if the total is zero
                    left += 1
                    # use a while loop to move the pinters with contions same as the if on line 7
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                               
                               
        return res