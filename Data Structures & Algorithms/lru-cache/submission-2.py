class Node: # a doubly ll

    def __init__(self, key: int, value: int, prev: Optional[Node] = None, next: Optional[Node] = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}

        self.dhead = Node(-1, -1)
        self.dtail = Node(-1, -1)
        self.dhead.next = self.dtail
        self.dtail.prev = self.dhead

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, cur: Node, newNode: Node):
        cur.next.prev = newNode
        newNode.next = cur.next
        newNode.prev = cur
        cur.next = newNode

    def get(self, key: int) -> int:
        if key in self.store:
            target = self.store[key]
            self.remove(target)
            self.insert(self.dhead, target)
            return target.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            target = self.store[key]
            self.remove(target)
            target.value = value
            self.insert(self.dhead, target)
        else:
            if len(self.store) == self.capacity:
                # evict LRU node
                del self.store[self.dtail.prev.key]
                self.remove(self.dtail.prev)
            newNode = Node(key, value)
            self.insert(self.dhead, newNode)
            self.store[key] = newNode
        
