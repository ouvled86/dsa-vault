# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        Q = []
        ret = []
        Q.append(root)

        while Q:
            Qlen = len(Q)
            inner = []
            for e in range(Qlen):
                curr = Q.pop(0)
                inner.append(curr.val)
                if curr.left: Q.append(curr.left)
                if curr.right: Q.append(curr.right)
            if inner:
                ret.append(inner)
            
        return ret

