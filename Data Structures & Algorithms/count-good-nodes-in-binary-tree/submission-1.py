# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        cunt = 0

        def fun(root,maxi):
            nonlocal cunt 
            if not root:
                return 
            if root.val >= maxi:
                cunt += 1 
                maxi = root.val 
            fun(root.left,maxi)
            fun(root.right,maxi)
        
        fun(root,root.val) 
        return cunt 