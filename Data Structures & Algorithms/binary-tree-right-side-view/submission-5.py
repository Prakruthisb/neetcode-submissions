# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []

        q = deque([(root,0)])
        while q:
            node,c = q.popleft()
            if c==len(ans):
                ans.append(node.val)
            if node.right:
                q.append((node.right,c+1))
            if node.left:
                q.append((node.left,c+1))
        return ans 