# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def helper(root):
            if not root:
                return []
            
            stack = [root]
            res = []
            
            while stack:
                node = stack.pop()
                if node:
                    if not node.left and not node.right:
                        res.append(node.val)
                        
                    if node.left:
                        stack.append(node.left)
                        
                    if node.right:
                        stack.append(node.right)
                        
            return res
        
        l1 = helper(root1)
        l2 = helper(root2)
        
        
        return l1 == l2
                        
                        
            
            