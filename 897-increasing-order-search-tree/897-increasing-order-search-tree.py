# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.curr = TreeNode()
        
        self.res = self.curr
        
        def inorder(node):
            if node.left:
                inorder(node.left)
                
            self.curr.right = TreeNode()
            self.curr = self.curr.right
            self.curr.val = node.val
            
            if node.right:
                inorder(node.right)
                
            
        inorder(root)
        
        return self.res.right