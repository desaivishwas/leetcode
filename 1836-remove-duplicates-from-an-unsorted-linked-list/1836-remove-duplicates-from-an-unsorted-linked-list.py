# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        d =  defaultdict(int)
        dummy = ListNode(0)
        prev = dummy
        
        n, node = head, head
        
        while n:
            d[n.val] += 1
            n = n.next
            
            
        while node:
            if d[node.val] == 1:
                prev.next = ListNode(node.val)
                prev = prev.next
            node = node.next
            
        return dummy.next
        
        
        