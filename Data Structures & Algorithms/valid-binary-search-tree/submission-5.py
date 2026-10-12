# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ret = True

        def dfs(curr, last_min, last_max):
            if not curr: return

            nonlocal ret
            if curr.val <= last_min or curr.val >= last_max:
                ret = False

            dfs(curr.left, last_min, curr.val)
            dfs(curr.right, curr.val, last_max)
        
        dfs(root, -1000000000, 1000000000)
        return ret

