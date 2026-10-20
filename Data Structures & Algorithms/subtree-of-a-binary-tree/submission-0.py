# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r1,r2):
            if not r1 and not r2:
                return True 
            if not r1 or not r2:
                return False 
            if r1.val != r2.val:
                return False 
            return isSame(r1.left,r2.left) and isSame(r1.right,r2.right)
        
        def fun(root):
            if not root:
                return False
            if root.val == subRoot.val:
                if isSame(root,subRoot):
                    return True 
            return fun(root.left) or fun(root.right)
        
        return fun(root)