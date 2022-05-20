# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # for elemantary addition
        carry = 0
        
        temp = ListNode()
        curr = temp
        
        while l1 or l2 or carry:
            
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            # carry
            val  =  v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
            
            
            # updating the pointers
            curr = curr.next
            # move the pointers in l1 and l2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return temp.next
            
            
            
            
            
            
            
            
        