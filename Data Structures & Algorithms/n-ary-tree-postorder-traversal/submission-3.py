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

        def traverse(root):
            if not root:
                return None
            
            for child in root.children:
                traverse(child)

            self.ans.append(root.val)
        traverse(root)
        return self.ans