class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0
        i, l = 0, len(heaters) - 2
        for house in houses:
            while i <= l and (abs(house - heaters[i]) >= abs(house - heaters[i+1])):
                i += 1
            else:
                radius = max(radius, abs(house - heaters[i]))
                
        return radius
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
				# houses.sort()
				# heaters.sort()
				# mrad=0
				# i=0
				# l=len(heaters)-2
				# for house in houses:
				# while i<=l and (abs(house-heaters[i])>=abs(house-heaters[i+1])):
				# i+=1
				# else:
				# mrad=max(mrad, abs(house-heaters[i]))
				# return mrad