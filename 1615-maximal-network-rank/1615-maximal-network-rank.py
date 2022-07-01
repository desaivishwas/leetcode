class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for u,v in roads:
            graph[u].append(v)
            graph[v].append(u)
            
        res = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                roadLen = len(graph[i]) + len(graph[j])
                
                if j in graph[i]:
                    roadLen -= 1
                    
                res = max(res, roadLen)
                
                
        return res
                
                