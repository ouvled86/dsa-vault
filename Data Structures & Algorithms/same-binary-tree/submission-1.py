# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        bfs = [q, p]

        while bfs:
            node_q = bfs.pop()
            node_p = bfs.pop()
            if node_p and node_q:
                if node_q.val == node_p.val:
                    bfs.append(node_q.left)
                    bfs.append(node_p.left)
                    bfs.append(node_q.right)
                    bfs.append(node_p.right)
                else:
                    return False
            elif node_p or node_q:
                return False
        
        return True

