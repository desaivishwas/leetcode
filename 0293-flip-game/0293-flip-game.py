class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        
        res = []
        r = 1
        if len(currentState) <= 1:
            return res
        
        while r < len(currentState):
            if currentState[r - 1] + currentState[r] == '++':
                res.append(currentState[0:r - 1] + "--" + currentState[r + 1:])
            r += 1
            
        return res
        