# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(path, running):
            nonlocal res
            
            if not path:
                return
            
            running += path.val
            
            if running - targetSum in d:
                res += d[running - targetSum]
            
            d[running] += 1
            
            dfs(path.left, running)
            dfs(path.right, running)
            
            
            d[running] -= 1
        
        
        res = 0
        d = defaultdict(int)
        d[0] = 1
        dfs(root, 0)
        
        return res
        
        
        
        
        
        