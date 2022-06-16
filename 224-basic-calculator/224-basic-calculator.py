from collections import deque

class Solution:
    # dfs
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')
        queue = deque(s)
        return self.dfs(queue)
        
    def dfs(self, q):
        res, num, sign = [], 0, 1

        while q:
            a = q.popleft()
            if a == "(":
                # recurisvely go to next level 
                num = self.dfs(q)

            if a.isdigit():
                num = num * 10 + int(a)

            if not q or not a.isdigit():
                if sign == 1:
                    res.append(num)
                else:
                    res.append(-1 * num)

                sign = 1 if a == '+' else -1
                num = 0

            if a == ")":
                break

        return sum(res)
            
        
    
        