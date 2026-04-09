class Node:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.occupied = 0
        self.dhead = Node(-1, -1)
        self.dtail = Node(-1, -1)
        self.store = {} # empty hash map

        self.dhead.next = self.dtail
        self.dtail.prev = self.dhead

    def remove(self, node: Node):
        tnext = node.next
        tprev = node.prev
        node.prev.next = tnext
        node.next.prev = tprev

        self.occupied -= 1

    def insert(self, node: Node, newNode: Node): # inserts a new node with value `value` after `node`
        newNode.prev = node
        newNode.next = node.next
        node.next.prev = newNode
        node.next = newNode

        self.occupied += 1

    def get(self, key: int) -> int:
        if key in self.store:
            foundNode = self.store[key]
            ret = foundNode.value
            self.remove(foundNode)
            newNode = Node(key, ret)
            self.insert(self.dhead, newNode)
            self.store[key] = newNode
            return ret
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            foundNode = self.store[key]
            self.remove(foundNode)
            newNode = Node(key, value)
            self.insert(self.dhead, newNode)
            self.store[key] = newNode
        else:
            if self.occupied == self.capacity:
                # evict tail
                del self.store[self.dtail.prev.key]
                self.remove(self.dtail.prev)
            newNode = Node(key, value)
            self.insert(self.dhead, newNode)
            self.store[key] = newNode


