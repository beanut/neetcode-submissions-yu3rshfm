# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, listOne: Optional[ListNode], listTwo: Optional[ListNode]) -> Optional[ListNode]:
        p = listOne
        q = listTwo
        dhead = ListNode(-1)
        cur = dhead

        while p or q:
            while p and (not q or p.val <= q.val):
                cur.next = p
                cur = cur.next
                p = p.next
            while q and (not p or q.val <= p.val):
                cur.next = q
                cur = cur.next
                q = q.next
        
        cur.next = None

        return dhead.next

    def mergeRange(self, lists: List[Optional[ListNode]], l: int, r: int) -> Optional[ListNode]:
        # base case
        if l == r:
            if lists[l] == None:
                return None
            else:
                return lists[l]
        
        mid = (l + r) // 2

        return self.mergeTwoLists(self.mergeRange(lists, l, mid), self.mergeRange(lists, mid + 1, r))

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        return self.mergeRange(lists, 0, len(lists) - 1)