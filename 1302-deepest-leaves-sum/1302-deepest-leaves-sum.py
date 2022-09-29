# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepSum, depth = 0, 0
        
        stack = [(root, 0)]
        
        while stack:
            node, curr = stack.pop()
            if node:
                if not node.left and not node.right:
                    if depth < curr:
                        deepSum = node.val
                        depth = curr
                    elif depth == curr:
                        deepSum += node.val
                        
                else:
                    if node.left:
                        stack.append((node.left, curr + 1))
                    if node.right:
                        stack.append((node.right, curr + 1))

        return deepSum