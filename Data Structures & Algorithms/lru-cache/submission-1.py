class LRUCache:
    class Node:
        def __init__(self, x: int, y: int, next: 'Node' = None, prev: 'Node' = None):
            self.key = int(x)
            self.val = int(y)
            self.next = next
            self.prev = prev
    
    def __init__(self, capacity: int):
        self.store = {}
        self.capacity = capacity
        self.lrup = LRUCache.Node(-1, -1)
        self.mrup = LRUCache.Node(-1, -1)
        self.lrup.next = self.mrup
        self.mrup.prev = self.lrup

    def insertNode(self, n: Node):
        pv = self.mrup.prev
        nx = self.mrup
        pv.next = n
        nx.prev = n
        n.prev = pv
        n.next = nx


    def deleteNode(self, n: Node):
        n.prev.next = n.next
        n.next.prev = n.prev

    def get(self, key: int) -> int:
        if key in self.store:
            self.deleteNode(self.store[key])
            self.insertNode(self.store[key])
            return self.store[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.deleteNode(self.store[key])
        self.store[key] = self.Node(key, value)
        self.insertNode(self.store[key])

        if len(self.store) > self.capacity:
            del self.store[self.lrup.next.key]
            self.deleteNode(self.lrup.next)

        
