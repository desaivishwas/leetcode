# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        copy = []
        curr = head
        while curr is not None:
            copy.append(curr.val)
            curr = curr.next
            
        return copy == copy[::-1]