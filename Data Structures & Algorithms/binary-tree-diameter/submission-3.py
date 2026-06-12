# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        
        def maxdepth(root):
            if not root:
                return 0

            return 1+max(maxdepth(root.left), maxdepth(root.right))

        def traverse(root):
            if not root:
                return 0
            
            current_diameter = maxdepth(root.left) + maxdepth(root.right)
            self.ans = max(self.ans, current_diameter)
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        return self.ans


            