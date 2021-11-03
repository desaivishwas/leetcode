from typing import List

class Solution:
    def majorityElement( nums: List[int]) -> int:
        majority = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            count = max(count, majority)
        return count

    if __name__ == "__main__":
        x = [3,2,3]
        majorityElement(x)