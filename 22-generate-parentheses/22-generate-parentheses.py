class Solution(object):
    def generateParenthesis(self, n):
        res = []
        
        def backtrack(s, openP, closeP):
            
            if openP == closeP == n:
                res.append(s)
                
            if openP < n:
                backtrack(s + '(', openP + 1, closeP)
                
            if closeP < openP:
                backtrack(s + ')', openP, closeP + 1)
                
                
        backtrack('', 0, 0)
        
        return res
                