# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return []
        
        stack = [(root, 0)]
        
        while stack:
            node, lvl = stack.pop()
            if node:
                if len(levels) == lvl:
                    levels.append([])
                    
                levels[lvl].append(node.val)
                if node.right:
                    stack.append((node.right, lvl + 1))
                
                if node.left:
                    stack.append((node.left, lvl + 1))
                
                
                    
        return levels