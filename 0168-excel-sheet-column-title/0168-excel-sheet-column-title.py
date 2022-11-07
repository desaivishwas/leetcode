class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = 0
        result = ""
        while columnNumber:
            
            # get the residuum and the new number
            columnNumber, res = divmod(columnNumber-1, 26)
            
            # 65 = ord('A')
            result = chr(65 + res) + result
        return result