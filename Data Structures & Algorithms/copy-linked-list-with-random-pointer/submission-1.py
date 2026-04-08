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
        seen = {}

        cur = head

        while cur:
            seen[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        while cur:
            copy = seen[cur]
            copy.next = seen.get(cur.next, None)
            copy.random = seen.get(cur.random, None)
            cur = cur.next
        
        return seen.get(head, None)
            