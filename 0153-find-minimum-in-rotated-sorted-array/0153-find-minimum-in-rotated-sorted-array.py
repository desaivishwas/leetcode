class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                right = mid
            else:
                left = mid + 1
                