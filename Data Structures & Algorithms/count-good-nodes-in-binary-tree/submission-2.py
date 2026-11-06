# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, greatest):
            if not node:
                return 0
            
            res = 1 if node.val >= greatest else 0
            greatest = max(greatest, node.val)
            res += dfs(node.left, greatest)
            res += dfs(node.right, greatest)
            return res

        return dfs(root, root.val)

