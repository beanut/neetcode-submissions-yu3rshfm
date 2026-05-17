"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        def dfs(node):
            if not node:
                return None
        
            cloneNode = Node(node.val)
            seen[node.val] = cloneNode

            for n in node.neighbors:
                if n.val in seen:
                    cloneNode.neighbors.append(seen[n.val])
                else:
                    cloneNode.neighbors.append(dfs(n))
            
            return cloneNode
        
        return dfs(node)

            
        