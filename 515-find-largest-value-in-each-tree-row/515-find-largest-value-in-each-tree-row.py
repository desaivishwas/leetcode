# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        # DFS based solution
        # Time and Space: O(n)
        
        largest = []
        
        def helper(node, level):
            
            if not node:
                return 
            
            if level >= len(largest):
                largest.append(node.val)
            else:
                largest[level] = max(largest[level], node.val)
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        helper(root, 0)
        return largest

                
                
                
        
        
        
        
        
        
        
        
        
        