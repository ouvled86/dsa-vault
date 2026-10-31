# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        bfs_q = [q]
        bfs_p = [p]

        while bfs_q and bfs_p:
            node_q = bfs_q.pop()
            node_p = bfs_p.pop()
            if node_p and node_q:
                if node_q.val == node_p.val:
                    bfs_q.append(node_q.left)
                    bfs_q.append(node_q.right)
                    bfs_p.append(node_p.left)
                    bfs_p.append(node_p.right)
                else:
                    return False
            elif node_p or node_q:
                return False
        
        if bfs_q or bfs_p:
            return False
        
        return True

