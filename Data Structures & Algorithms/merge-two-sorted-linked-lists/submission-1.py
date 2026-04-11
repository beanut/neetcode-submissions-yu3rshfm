# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = list1
        q = list2
        dhead = ListNode(-1)
        cur = dhead

        while p or q:
            while p and (not q or p.val <= q.val):
                cur.next = p
                p = p.next
                cur = cur.next
            while q and (not p or q.val <= p.val):
                cur.next = q
                q = q.next
                cur = cur.next

        cur.next = None

        return dhead.next