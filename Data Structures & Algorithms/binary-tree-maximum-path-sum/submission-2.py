# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float('-inf')

        def fun(root):
            nonlocal maxi
            if not root:
                return 0 
            l = fun(root.left)
            r = fun(root.right)
            val = root.val+l+r
            maxi = max(maxi,val)
            return 0 if val<0 else root.val+max(l,r)
        
        fun(root)
        return maxi