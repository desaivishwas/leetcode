class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # directions
        # putting robot in north direction
        X, Y = 0, 1 # North
        x, y = 0,0 
        
        for dir in instructions:
            if dir == "G":
                x,y = x + X, y + Y
                
            elif dir == "L":
                X, Y = -1 * Y, X
                
            else:
                X, Y = Y, -1 * X
                
        return (X, Y) != (0,1) or (x,y) == (0,0)
                
         