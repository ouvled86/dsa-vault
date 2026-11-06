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
        res = 1
        greatest = root.val

        def dfs(node, greatest):
            if not node:
                return
            nonlocal res
            if node.val >= greatest:
                res += 1
            dfs(node.left, max(node.val, greatest))
            dfs(node.right, max(node.val, greatest))

        dfs(root.left, greatest)
        dfs(root.right, greatest)
        return res

