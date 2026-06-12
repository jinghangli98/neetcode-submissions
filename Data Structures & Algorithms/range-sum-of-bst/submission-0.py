# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        

        self.ans = 0
        def traverse(node, low, high):
            if not node:
                return 0
            
            if low<=node.val and node.val <=high:
                self.ans += node.val
            
            traverse(node.left, low, high)
            traverse(node.right, low, high)
        
        traverse(root, low, high)

        return self.ans

        

