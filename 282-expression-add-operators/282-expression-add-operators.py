class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        output = []
        
        def dfs(expr, index, total, prev_sum):
            
            if index == len(num) and total == target:
                output.append(expr)
            
            for j in range(index+1, len(num)+1):  #j should be greate than index and substring is inclusive in python
                strr = num[index:j]
                curr = int(strr)
                
                if num[index] == '0' and strr != '0':
                    continue
                
                if not expr:
                    dfs(strr, j, curr, curr)
                else:
                    dfs(expr + '+' + strr, j, total + curr, curr)
                    
                    dfs(expr + '-' + strr, j, total - curr, -curr)
                    
                    dfs(expr + '*' + strr, j, total - prev_sum + prev_sum * curr, prev_sum * curr )

        dfs('', 0, 0, 0)
        return output
        