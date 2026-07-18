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
        #prev is reverse of the second half, #head is the first half 

        first = head
        while prev:
            tmp1 = first.next
            tmp2 = prev.next

            first.next = prev
            prev.next = tmp1

            first = tmp1
            prev = tmp2
        





