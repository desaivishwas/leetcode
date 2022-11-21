class Solution:
    def dfs(self, i, stones, visited):
        visited.add(i)

        for j in range(len(stones)):
            if (stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]) and j not in visited:
                self.dfs(j, stones, visited)



    def removeStones(self, stones: List[List[int]]) -> int:
        visited = set()
        
        cnt = 0
        for i in range(len(stones)):
            if i not in visited:
                self.dfs(i, stones, visited)
                cnt += 1
        
        return len(stones) - cnt
                    
        