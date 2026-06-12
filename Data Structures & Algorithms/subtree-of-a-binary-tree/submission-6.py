# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        self.subtree = False
        def sameTree(r1, r2):
            if not r1 and not r2:
                return True
            
            if not r1 or not r2:
                return False
            
            if r1.val != r2.val:
                return False
            
            return sameTree(r1.left, r2.left) and sameTree(r1.right, r2.right)
        
        def traverse(root, subRoot):
            if not root:
                return None
            
            if sameTree(root, subRoot):
                self.subtree = True
            
            traverse(root.left, subRoot)
            traverse(root.right, subRoot)
        
        traverse(root, subRoot)
        return self.subtree






        
