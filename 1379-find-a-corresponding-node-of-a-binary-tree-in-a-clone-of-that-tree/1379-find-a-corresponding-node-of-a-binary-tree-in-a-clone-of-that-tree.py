# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        res = 0
        def inorder(og, clone):
            nonlocal res
            if og:
                inorder(og.left, clone.left)
                if og is target:
                    res = clone
                    
                inorder(og.right, clone.right)
                
                
        inorder(original, cloned)
        return res
        