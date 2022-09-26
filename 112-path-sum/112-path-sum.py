# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        
        stack = [(root, targetSum - root.val),]
        
        while stack:
            node, curr = stack.pop()
            if not node.left and not node.right and curr == 0:
                return True
            if node.right:
                stack.append((node.right, curr - node.right.val))
            if node.left:
                stack.append((node.left, curr - node.left.val))
                
                
                
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not root:
#             return False

#         currSum -= root.val
#         if not root.left and not root.right:  # if reach a leaf
#             return currSum == 0
#         return self.hasPathSum(root.left, currSum) or self.hasPathSum(root.right, currSum)
        