# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None 
        p = 0 
        h = {}
        for i in range(len(inorder)):
            h[inorder[i]] = i
        
        def dfs(l,r):
            if l>=r:
                return None
            nonlocal p
            root = TreeNode(preorder[p])
            mid = h[preorder[p]]
            p += 1 
            root.left = dfs(l,mid)
            root.right = dfs(mid+1,r)
            return root 
        
        return dfs(0,len(inorder))