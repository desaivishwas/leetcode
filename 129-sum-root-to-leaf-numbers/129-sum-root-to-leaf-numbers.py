# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        num = 0
        
        stack = [(root, root.val)]
        
        while stack:
            node, path_sum = stack.pop()
            
            if not node.left and not node.right:
                num += path_sum
                
            if node.left:
                stack.append((node.left, path_sum * 10 + node.left.val))
                
            if node.right:
                stack.append((node.right, path_sum * 10 + node.right.val))
                
                
        return num