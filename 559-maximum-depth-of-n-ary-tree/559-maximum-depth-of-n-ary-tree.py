"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        depth = 0
        
        while stack:
            node, curr = stack.pop()
            
            if node:
                depth = max(depth, curr)
                
            for c in node.children:
                stack.append((c, curr + 1))
            
            
        return depth