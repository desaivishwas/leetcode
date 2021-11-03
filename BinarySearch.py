class Solution:
    def search(self, nums: List[int], target: int) -> int:
         # Brute force
        """ 
        O(n)
        for i in range(len(nums)):
            if target == nums[i]:
                x= i
                break
            else:
                x = -1
        return x
        """
        # O(logn)
        left = 0
        right = len(nums)-1
        while(left<=right):
            pivot = left + (right-left) // 2
            # if our middlemost element is our target
            if nums[pivot] == target:
                return pivot
            # searching on the right
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot -1
        return -1