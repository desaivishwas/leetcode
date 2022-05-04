class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = { i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            d[c].append(p)
            
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if d[course] == []:
                return True
            
            visited.add(course)
            for pre in d[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            d[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True