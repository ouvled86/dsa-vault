# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        table = {val: i for i, val in enumerate(inorder)}
        self.i = 0

        def dfs(l, r):
            if l > r:
                return None

            curr_val = preorder[self.i]
            self.i += 1
            root = TreeNode(curr_val)
            half = table[curr_val]
            root.left = dfs(l, half - 1)
            root.right = dfs(half + 1, r)
            return root
        
        root = dfs(0, len(preorder) - 1)
        return root