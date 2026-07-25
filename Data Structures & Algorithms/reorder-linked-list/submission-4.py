# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        curr = prev
        while curr:
            tmp1 = head.next
            tmp2 = curr.next

            head.next = curr
            curr.next = tmp1

            head = tmp1
            curr = tmp2
        






