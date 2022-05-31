# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        carry = 0
        while l1 is not None or l2 is not None:
            result = carry
            if l1 is not None:
                result += l1.val
                l1 = l1.next
            if l2 is not None:
                result += l2.val
                l2 = l2.next
            current.next = ListNode(result%10)
            if result > 9:
                carry = 1
            else:
                carry = 0
            current = current.next
		#adds the overflow carry to end of the ouutput linked list
        if carry == 1:
            current.next = ListNode(carry)
        return head.next