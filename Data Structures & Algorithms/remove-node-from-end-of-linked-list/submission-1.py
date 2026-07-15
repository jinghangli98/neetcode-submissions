# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def reverselist(head):

            prev = None
            while head:
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            
            return prev
        
        prev = reverselist(head)
        node = prev

        if n == 1:
            prev = prev.next
        else:
            for _ in range(n-2):
                node = node.next
            node.next = node.next.next

        return reverselist(prev)




            
            
