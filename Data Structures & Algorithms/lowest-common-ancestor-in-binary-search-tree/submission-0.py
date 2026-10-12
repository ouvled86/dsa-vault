# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        common_ancestor = root
        curr_p = root
        curr_q = root
        while curr_p != None and curr_q != None:
            if curr_p.val == curr_q.val:
                common_ancestor = curr_p

            if curr_p == p or curr_q == q: break

            if p.val < curr_p.val: curr_p = curr_p.left
            else: curr_p = curr_p.right
            if q.val < curr_q.val: curr_q = curr_q.left
            else: curr_q = curr_q.right

        return common_ancestor

