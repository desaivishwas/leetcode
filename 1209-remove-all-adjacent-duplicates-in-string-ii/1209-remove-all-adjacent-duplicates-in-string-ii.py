class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # [char, count]
        stack = []
        # iterate through loop
        for c in s:
            # if stack not empty and char is same as stack
            if stack and stack[-1][0] == c:
                # incremnt the count of the char
                stack[-1][1] += 1
            else:
                # append the char to the stack with count = 1
                stack.append([c, 1])
                
            # if count == k then pop from the stack
            if stack[-1][1] == k:
                stack.pop()
                
        # gettinh the result        
        res = ""
        for char, count in stack:
            # multply remaining char by its count
            res += (char * count)
            
        return res