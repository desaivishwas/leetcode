class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        d = {}
        for i in range(len(rooms)):
            d[i] = rooms[i]
            
        visited = set()
        
        def dfs(n):
            visited.add(n)
            
            for neighbour in d.get(n):
                if neighbour not in visited:
                    dfs(neighbour)
                    
        dfs(0)
        
        return len(visited) == len(rooms)