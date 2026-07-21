# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def reverse(nodes):
            prev = None
            while nodes:
                tmp = nodes.next
                nodes.next = prev
                prev = nodes
                nodes = tmp
            
            return prev
        
        reversed_nodes = reverse(head)
        curr = reversed_nodes
        if n == 1:
            reversed_nodes = reversed_nodes.next
        else:
            for _ in range(n - 2):
                curr = curr.next
            
            curr.next = curr.next.next

        return reverse(reversed_nodes)
