# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right\


from collections import deque, defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        q = deque([(root, 0)])
        levels = defaultdict(list)
        
        while q:
            node, level = q.popleft()
            
            levels[level].append(node.val)
            
            if node.left:
                q.append((node.left, level + 1))
                
            if node.right:
                q.append((node.right, level + 1))
                
        return levels.values()