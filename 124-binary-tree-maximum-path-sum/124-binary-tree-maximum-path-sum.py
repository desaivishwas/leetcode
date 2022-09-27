# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            
            
            max_left = dfs(root.left)
            max_right = dfs(root.right)
            
            max_left = max(max_left, 0)
            max_right = max(max_right, 0)
            
            
            res[0] = max(res[0], root.val + max_left + max_right)
            
            
            return root.val + max(max_left, max_right)
        
        
        dfs(root)
        
        return res[0]
             