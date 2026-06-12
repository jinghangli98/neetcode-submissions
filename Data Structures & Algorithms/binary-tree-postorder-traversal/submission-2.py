# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        def traverse(root):
            if not root:
                return None
            
            traverse(root.left)
            traverse(root.right)
            self.ans.append(root.val)
        
        traverse(root)
        return self.ans