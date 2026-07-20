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
        
        nexthalf = slow.next
        slow.next = None

        def reverse(nodes):
            prev = None
            while nodes:
                tmp = nodes.next
                nodes.next = prev
                prev = nodes
                nodes = tmp
            
            return prev
        
        nexthalf = reverse(nexthalf)
        firsthalf = head
        
        while nexthalf:
            tmp1 = firsthalf.next
            tmp2 = nexthalf.next

            firsthalf.next = nexthalf
            nexthalf.next = tmp1

            firsthalf = tmp1
            nexthalf = tmp2
        

            



