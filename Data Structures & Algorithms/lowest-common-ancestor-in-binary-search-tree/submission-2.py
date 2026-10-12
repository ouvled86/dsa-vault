# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        common_ancestor = root

        while common_ancestor:
            if common_ancestor.val > max(p.val, q.val):
                common_ancestor = common_ancestor.left
            elif common_ancestor.val < min(p.val, q.val):
                common_ancestor = common_ancestor.right
            else: break

        return common_ancestor

