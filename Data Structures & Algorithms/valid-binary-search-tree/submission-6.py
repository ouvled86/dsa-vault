# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr, last_min, last_max):
            if not curr: return True

            if curr.val <= last_min or curr.val >= last_max: return False

            return dfs(curr.left, last_min, curr.val) and dfs(curr.right, curr.val, last_max)
        
        return dfs(root, float('-inf'), float('inf'))

