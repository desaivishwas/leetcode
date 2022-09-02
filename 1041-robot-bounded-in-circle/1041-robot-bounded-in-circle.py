class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # directions
        dirX, dirY = 0, 1  # north direction
        x, y = 0, 0
        
        for d in instructions:
            if d == "G":
                x, y = x + dirX, y + dirY
            elif d == "L":
                # anti clockwise - swap the directions
                dirX, dirY = -1 * dirY, dirX
            else:
                dirX, dirY = dirY, -1*dirX
        
        
        return (x, y) == (0,0) or (dirX, dirY) != (0, 1)