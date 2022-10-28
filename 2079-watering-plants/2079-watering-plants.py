class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        curr = capacity
        i = 0
        steps = 0
        while i < len(plants):
            if plants[i] > curr:
                curr = capacity 
                steps += (2 * i)
            else:
                curr -= plants[i]
                steps += 1
                plants[i] = -1
                
            if plants[i] == -1:
                i += 1
                
        return steps
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
			# curr_cap, index = capacity, 0
			# size = len(plants)
			# result = 0
			# while index < size:
			# if plants[index] < curr_cap:
			# curr_cap = capacity
			# result += (2 * index)
			# else:
			# curr_cap -= plants[index]
			# result += 1
			# plants[index] = -1
			# # This will make sure that the current index is not watered until the can is filled
			# if plants[index] == -1:
			# index += 1
			# return result