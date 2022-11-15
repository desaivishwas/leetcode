# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def getHeight(node):
            if(not node):
                return 0
            
            return 1 + getHeight(node.left)
        
        h = getHeight(root) - 1
        res = (2 ** h) - 1 
        
        def binary_search(right,level): 
            if(not right):
                return True
            
            if(level==h):
                return False
            
            return binary_search(right.left,level+1)
        
        left = root.left 
        right = root.right
        currLevel = 1
        
        while(currLevel < h and left and right): 
            if(binary_search(right,currLevel)): 
                left, right = left.left, left.right
                
            else:
                left, right = right.left, right.right
                res += (2 ** (h - currLevel))

            currLevel+=1
            
        if right:
            res += 2
        else:
            res += 1
        
        return res
        