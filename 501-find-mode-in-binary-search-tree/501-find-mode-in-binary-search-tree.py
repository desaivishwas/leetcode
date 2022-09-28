# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 0
        
        d = {}
        
        stack = [root]
        
        while stack:
            node = stack.pop()
                
            if node.val in d:
                d[node.val] += 1
            else:
                d[node.val] = 1
                
                
            if node.left:
                stack.append(node.left)
                
            if node.right:
                stack.append(node.right)
                
                
        value = max(d.values())
        res = []
        for k,v in d.items():
            if v == value:
                res.append(k)
                
        return res