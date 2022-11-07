class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_num = {}
        stack = []
        
        for num2 in nums2:
            while stack and stack[-1] < num2:
                num1 = stack.pop()
                next_num[num1] = num2
            stack.append(num2)
                 
        while stack:
            num1 = stack.pop()
            next_num[num1] = -1
                  
        res = [next_num[num1] for num1 in nums1]      
        return res