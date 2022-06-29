class Solution:
    
    def dfs(self,node,vis,graph,color):
        ans = True
        for adjcent in graph[node]:
            if color == vis[adjcent]:
                return False
            if vis[adjcent] == -1:
                vis[adjcent] = abs(1-color)
                ans &= self.dfs(adjcent,vis,graph,vis[adjcent])
        return ans
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [-1] * n 
        for node in range(n):
            if visited[node] == -1:
                visited[node] = 1
                if not self.dfs(node, visited, graph, 1):
                    return False
        return True
        