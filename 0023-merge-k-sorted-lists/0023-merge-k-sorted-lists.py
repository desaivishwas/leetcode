# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                node.append(l.val)
                l = l.next
                
        for x in sorted(node):
            point.next = ListNode(x)
            point = point.next
            
        
        return head.next