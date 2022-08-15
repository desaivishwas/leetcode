# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while (p.val < root.val and q.val < root.val) or (p.val > root.val and q.val > root.val):
            if p.val < root.val:
                root = root.left
            else:
                root = root.right
                
                
        return root