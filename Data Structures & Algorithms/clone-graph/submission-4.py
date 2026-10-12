"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        if not node.neighbors: return Node(val=1)
        ret = Node()
        visited = {}
    
        def dfs(src, dst, visited):
            dst.val = src.val
            visited[src] = dst
            
            for n in src.neighbors:
                if n in visited:
                    dst.neighbors.append(visited[n])
                if n not in visited:
                    dst.neighbors.append(Node())
                    dfs(n, dst.neighbors[-1], visited)
                    
        
        dfs(node, ret, visited)


       
        return ret
