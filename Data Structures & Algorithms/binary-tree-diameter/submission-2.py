# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        def find_d(root):
            nonlocal ans 
            if not root:
                return 0
            l = find_d(root.left)
            r = find_d(root.right)
            ans = max(ans,l+r)
            return 1+max(l,r)
        
        find_d(root)
        return ans 