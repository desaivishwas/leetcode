# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        
        stack = [(root, [])]
        
        while stack:
            
            node, path = stack.pop()
            
            if not node: continue 
                
            if not node.left and not node.right: 
                
                if path + [node.val] == arr: return True
                continue
                
            stack.append((node.left, path + [node.val]))
            stack.append((node.right, path + [node.val]))
            
        return False