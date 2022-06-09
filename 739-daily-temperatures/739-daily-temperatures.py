class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)  
        for curr_index, curr_temp in enumerate(temperatures):
            while stack and stack[-1][0] < curr_temp:
                stack_temp, prev_index = stack.pop()
                res[prev_index] = curr_index - prev_index
            stack.append([curr_temp, curr_index])
        return res

        