class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        def helper(n):
            n = str(n)
            say = ""
            curr = n[0]
            count = 1
            for dig in n[1:]:
                if dig == curr:
                    count += 1
                else:
                    say += str(count) + curr
                    curr = dig
                    count = 1
            say += str(count) + curr
            return say
        
        return helper(self.countAndSay(n-1))
        