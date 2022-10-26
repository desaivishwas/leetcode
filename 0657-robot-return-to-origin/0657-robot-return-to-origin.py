class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if not moves:
            return True
        
        
        return moves.count("U") ==  moves.count("D") and moves.count("L") ==  moves.count("R")
            
        
#         x, y = 0, 0
#         for dir in moves:
#             if dir == "U": y -= 1
#             elif dir == "D": y += 1
#             elif dir == "L": x-= 1
#             else: x += 1
                
#         return x == y == 0