"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        tmp = head
        copy = Node(0)
        tba = defaultdict(list)
        visited = {}

        tmp2 = copy
        while tmp:
            tmp2.next = Node(tmp.val)
            tmp2 = tmp2.next
            if tmp in tba:
                for n in tba[tmp]:
                    n.random = tmp2
            visited[tmp] = tmp2
            if not tmp.random:
                tmp2.random = None
            else:
                if tmp.random in visited:
                    tmp2.random = visited[tmp.random]
                else:
                    tba[tmp.random].append(tmp2)
            tmp = tmp.next
        

        return copy.next