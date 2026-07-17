# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def reverse(head):
            prev = None
            while head:
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            
            return prev
        
        head = reverse(head)

        curr = head
        if n == 1:
            head = head.next
        else:
            for _ in range(n-2):
                curr = curr.next
        
            curr.next = curr.next.next

        return reverse(head)
