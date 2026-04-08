# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeSet = set()
        cur = head
        while cur:
            if cur in nodeSet:
                return True
            nodeSet.add(cur)
            cur = cur.next
        return False