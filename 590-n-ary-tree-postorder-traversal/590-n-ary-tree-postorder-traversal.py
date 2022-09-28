"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        res = []
        stack  = [root, ]
        
        while stack:
            node = stack.pop()
            
            if node:
                res.append(node.val)
                
            for child in node.children:
                stack.append(child)
                
                
        return res[::-1]