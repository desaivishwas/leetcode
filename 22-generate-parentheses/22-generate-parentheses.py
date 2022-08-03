class Solution(object):
    def generateParenthesis(self, n):
        result = []
        def backtracking(p, left, right):
            if left < n:
                backtracking(p + '(', left + 1, right)
            if right < left:
                backtracking(p + ')', left, right + 1)
            if right == n:
                result.append(p),

        backtracking('', 0, 0)
        return result