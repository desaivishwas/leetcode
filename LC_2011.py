class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        """ Attempt 1 """
        # X = 0
        # for operation in operations:
        #     if operation == "--X" or operation=="X--":
        #         X = X - 1
        #     elif operation == "++X" or operation=="X++":
        #         X = X + 1
        #     else:
        #         X=0
        # return X
        
        """ Attempt 2"""
        X = 0
        for operation in operations:
            if "++" in operation: X+=1
            if  "--" in operation: X-=1
        return X