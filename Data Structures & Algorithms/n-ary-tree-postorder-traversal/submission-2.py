"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        self.ans = []
        def traverse(node):
            if not node:
                return None
            
            for child in node.children:
                traverse(child)
            
            self.ans.append(node.val)
        
        traverse(root)
        return self.ans
        