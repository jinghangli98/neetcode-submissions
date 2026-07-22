# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sametree(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return sametree(p.left, q.left) and sametree(p.right, q.right)

        self.subtree = False
        def traverse(root, subRoot):
            if not root:
                return None
            
            if sametree(root, subRoot):
                self.subtree = True
            
            traverse(root.left, subRoot) 
            traverse(root.right, subRoot)
        
        traverse(root, subRoot)

        return self.subtree

        

