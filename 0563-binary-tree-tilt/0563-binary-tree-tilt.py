# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tilt = 0
        def dfs(node):
            nonlocal tilt
            
            if not node:
                return 0
            
            lsum = dfs(node.left)
            rsum = dfs(node.right)
            t = abs(lsum - rsum)
            
            tilt += t
            
            return lsum + rsum + node.val
        
        dfs(root)
        
        return tilt