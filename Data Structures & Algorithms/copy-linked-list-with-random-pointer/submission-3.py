"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        copy_table = {None:None}
        curr = head
        while curr:
            newnode = Node(curr.val)
            copy_table[curr] = newnode
            curr = curr.next
        
        curr = head
        while curr:
            newnode = copy_table[curr]
            newnode.next = copy_table[curr.next]
            newnode.random = copy_table[curr.random]
            curr = curr.next
        
        return copy_table[head]