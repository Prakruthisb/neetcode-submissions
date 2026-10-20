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
        def fun(node,maxi):
            if not node:
                return 0
            good = 1 if node.val >= maxi else 0 
            maxi = max(maxi,node.val)
            return good + fun(node.left,maxi) + fun(node.right,maxi)
        
        return fun(root,root.val)
            