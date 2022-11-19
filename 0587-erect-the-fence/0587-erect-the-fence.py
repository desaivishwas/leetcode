class Solution:
    def orientation(self, p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (r[1] - q[1]) * (q[0] - p[0])
    
    
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) < 4:
            return trees
        
        trees.sort()
        n, hull = len(trees), []
        
        for point in trees:
            while len(hull) >= 2 and self.orientation(hull[-2], hull[-1], point) > 0:
                hull.pop()
            hull.append(point)
        
        for point in trees[::-1]:
            while len(hull) >= 2 and self.orientation(hull[-2], hull[-1], point) > 0:
                hull.pop()
            hull.append(point)
        
        return list(set(map(tuple, hull)))