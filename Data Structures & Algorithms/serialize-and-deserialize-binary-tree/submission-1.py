# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = ""
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                s+=str(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                s+='#'
            s+=','
        return s


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data[0] == '#':
            return None
        vals = data.split(',')
        vals.pop()
        root = TreeNode(int(vals[0]))
        cur = root
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if vals[i] != '#':
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i+=1
            if vals[i] != '#':
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i+=1
        return cur