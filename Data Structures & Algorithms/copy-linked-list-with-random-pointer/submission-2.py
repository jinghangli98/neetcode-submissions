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

        table = {None:None}
        curr = head
        while curr:
            newNode = Node(curr.val)
            table[curr] = newNode
            curr = curr.next
        
        curr = head
        while curr:
            newNode = table[curr]
            newNode.next = table[curr.next]
            newNode.random = table[curr.random]
            curr = curr.next
        
        return table[head]