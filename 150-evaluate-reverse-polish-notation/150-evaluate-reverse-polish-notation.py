class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
                continue
                
            num2 = stack.pop()
            num1 = stack.pop()
            
            res = 0
            if token == "+":
                res = num2 + num1
                
            elif token == "-":
                res = num1 - num2
                
            elif token == "*":
                res = num2 * num1
                
            else:
                res = int(num1/num2)
                
            stack.append(res)     
                
        return stack.pop()