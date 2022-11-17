class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        overlap_w = 0
        overlap_h = 0
        
        
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        
        overlap_w = min(ax2,bx2) - max(ax1, bx1)
        overlap_h = min(ay2, by2) - max(ay1, by1)
        
        overlapArea = max(overlap_w, 0) * max(overlap_h, 0)
        
        return area1 + area2 - overlapArea
        
        
        
    
    