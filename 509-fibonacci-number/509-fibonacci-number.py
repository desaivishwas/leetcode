class Solution:
    def fib(self, n: int) -> int:
        
        print(n)
        def helper(n, memo):
            if memo[n] is not None:
                return memo[n]
            # if n == 0:
            if n <= 1:
                res = n
            else:
                res = helper(n - 1, memo) + helper(n - 2, memo)

            memo[n] = res 
            return res
        
        memo = [None] * (n + 1)
        return helper(n, memo)