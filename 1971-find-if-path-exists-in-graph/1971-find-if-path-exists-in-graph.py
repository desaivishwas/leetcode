class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def dfs(graph, src, dest, v):
            if src == dest:
                return True
            
            v.add(src)
            for neighbor in graph[src]:
                if neighbor not in v:
                    if dfs(graph, neighbor, dest, v):
                        return True
                    
            return False        
        
        graph = defaultdict(list)
        visited = set()
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        return dfs(graph, source, destination, visited)
    