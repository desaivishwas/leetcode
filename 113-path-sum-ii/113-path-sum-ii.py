# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ''' DFS --> iterative approach O(N) and O(N)'''
        
        if not root:
            return []
        
        if not root.right and not root.left and root.val == targetSum:
            return [[root.val]]
        
        res = []
        stack = [(root,[root.val])]
        
        while stack:
            node, values = stack.pop()
            diff = targetSum - sum(values)
            l_node, r_node = node.left, node.right
            
            if l_node:
                if not l_node.left and not l_node.right and diff == l_node.val:
                    res.append(values + [l_node.val])
                    
                stack.append((l_node, values + [l_node.val]))
            
            if r_node:
                if not r_node.left and not r_node.right and diff == r_node.val:
                    res.append(values + [r_node.val])
                    
                stack.append((r_node, values + [r_node.val]))
                
        return res
                
                