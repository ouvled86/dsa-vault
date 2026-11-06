# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        bfs = deque()
        bfs.append(root)
        next_level = []

        while bfs:
            curr = bfs.popleft()
            if curr:
                if curr.left:
                    next_level.append(curr.left)
                if curr.right:
                    next_level.append(curr.right)
            if not bfs:
                if curr:
                    ret.append(curr.val)
                bfs.extend(next_level)
                next_level.clear()
        
        return ret