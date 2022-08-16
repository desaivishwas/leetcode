# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        
        slow = fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            # if cycle exist
            if slow == fast:
                runner1 = head
                runner2 = fast
                
                while runner1 != runner2:
                    runner1 = runner1.next
                    runner2 = runner2.next
                    
                    
                return runner1
            
            