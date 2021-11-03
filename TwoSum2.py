from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index = {}
        for i, value in enumerate(numbers): 
            diff = target - numbers[i] 
           
            if diff in index: 
                return [index[diff]+1, i+1]  
            else:
                index[value] = i  