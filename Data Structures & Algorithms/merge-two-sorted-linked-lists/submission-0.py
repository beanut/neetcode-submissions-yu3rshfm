# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = list1
        q = list2
        head = ListNode()
        cur = head

        while p or q:
            while p and (not q or p.val <= q.val):
                newNode = ListNode(p.val)
                cur.next = newNode
                cur = newNode
                p = p.next
            while q and (not p or q.val <= p.val):
                newNode = ListNode(q.val)
                cur.next = newNode
                cur = newNode
                q = q.next
        
        return head.next
            