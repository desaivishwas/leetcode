# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res, count = defaultdict(int), defaultdict(int)
        
        
        def dfs(node,level):
            if not node:
                return 0
            
            res[level] += node.val
            count[level] += 1
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
            
        dfs(root, 0)
        
        return [res[i]/count[i] for i in res]