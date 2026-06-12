# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.ans = 0
        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)

            diameter = left_height + right_height
            self.ans = max(self.ans, diameter)

            return 1 + max(height(node.left), height(node.right))
        
        height(root)

        return self.ans        
