# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        ''' DFS O(N) and O(N)'''
        
        def dfs(node):
            nonlocal res
            if not node:
                return 0,0
            
            left, num_left = dfs(node.left)
            right, num_right = dfs(node.right)
            
            total = num_left + num_right + 1
            
            if ((left + right + node.val) // total) == node.val:
                res += 1
                
            return left + right + node.val, total
        
    
        
        res = 0
        dfs(root)
        return res
              
