# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        res  = 0
        stack = [(root, "")]
        
        while(stack):
            node, path = stack.pop()
            
            if node:
                path += str(node.val)
            
                if not(node.left or node.right):
                    res += int(path, 2)

                else:
                    stack.append((node.left, path))
                    stack.append((node.right,path))
                
                
        return res
                
                
                