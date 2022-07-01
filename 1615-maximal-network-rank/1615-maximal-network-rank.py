class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        # bulidng an adjacency graph list
        
        for u,v in roads:
            graph[u].append(v)
            graph[v].append(u)
            
        res = 0
    
        for i in range(n):
            for j in range(i + 1, n):
                # calcualting the road length
                roadLen = len(graph[i]) + len(graph[j])
                # removing road connected to both cities
                if j in graph[i]:
                    roadLen -= 1
                    
                res = max(res, roadLen)
                
                
        return res
                
                