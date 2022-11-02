class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        ''' BFS approach '''
        
        q =  deque([(start, 0)])
        visited = {start}
        
        while q:
            node, steps = q.popleft()
            
            if node == end:
                return steps
            
            for c in "ACGT":
                for i in range(len(node)):
                    neigh = node[:i] + c + node[i+1:]
                    if neigh not in visited and neigh in bank:
                        q.append((neigh, steps + 1))
                        visited.add(neigh)
                        
        return -1
                
            