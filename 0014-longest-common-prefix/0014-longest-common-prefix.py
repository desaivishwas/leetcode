class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        test = strs[0]
        
        res = ""
        
        while i < len(test):
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != test[i]:
                    return res
            res += test[i]
            i += 1
            
        return res
        