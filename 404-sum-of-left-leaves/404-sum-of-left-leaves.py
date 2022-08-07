# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        res=0
        
        a=deque([root])
        while a:
            node=a.popleft()
            if node.left:
                if node.left.left==None and node.left.right==None:
                    res+=node.left.val
                else:
                    a.append(node.left)
            if node.right:
                a.append(node.right)
        return res
        