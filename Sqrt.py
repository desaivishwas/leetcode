class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
    
        low = 2
        high = x
        while(low<=high):
            mid = low + (high-low)//2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                sol = mid
                low = mid + 1
            else:
                high = mid -1
        return 1 if (x == 2 or x ==3)  else sol
            