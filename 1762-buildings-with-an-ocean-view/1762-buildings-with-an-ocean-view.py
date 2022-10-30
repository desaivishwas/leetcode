class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        stack = []
        for curr in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] < heights[curr]:
                stack.pop()
                
            if not stack:
                res.append(curr)
                
            stack.append(curr)
            
            
        return reversed(res)
                
                