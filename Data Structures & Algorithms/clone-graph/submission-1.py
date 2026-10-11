"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# lets try BFS for the love of the game lmao

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = deque([node])
        ret = Node(node.val)
        store = {node : ret}

        while q:
            cur = q.popleft()

            for n in cur.neighbors:
                if n not in store:
                    newNeigh = Node(n.val)
                    store[n] = newNeigh
                    q.append(n)
                store[cur].neighbors.append(store[n])
        
        return ret


