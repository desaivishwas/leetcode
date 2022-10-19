# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            stack = [(p, q)]
            while stack:
                p, q = stack.pop()

                if not p and not q:
                    continue

                if not p or not q or p.val != q.val:
                    return False

                stack.append((p.left, q.left))
                stack.append((p.right, q.right))

            return True
    
        if not subRoot: return True
        if not root: return False
        
        if sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        
            