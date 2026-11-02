# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True
            if (p and not q) or (not p and q):
                return False
            if p.val != q.val:
                return False
            
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        bfs = [root]
        while bfs:
            node = bfs.pop()
            if node:
                if node.val == subRoot.val and dfs(node, subRoot):
                    return True
                bfs.append(node.left)
                bfs.append(node.right)
        
        return False
            

        

        