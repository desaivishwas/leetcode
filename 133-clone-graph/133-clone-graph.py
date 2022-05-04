"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldNew = {}
        # call dfs
        def dfs(node):
            # check if node in dictionary
            if node in oldNew:
                return oldNew[node]
            # else create a copy of  the node
            copy  = Node(node.val)
            # add it to dcitonary mappinf old val to new val;
            oldNew[node] = copy
            # run dfs and clone neighbors of the inital node
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            # retunrn the copt after all neighbors are visited
            return copy
        # check for edge case where node can be null
        return dfs(node) if node else None