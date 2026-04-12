# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseNNodes(self, head: Optional[ListNode], n: int) -> (Optional[ListNode], Optional[ListNode]):
        cur = head
        prev = None
        for _ in range(n):
            tempnext = cur.next
            cur.next = prev
            prev = cur
            cur = tempnext
        head.next = cur
        return (prev, cur)

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # precompute len
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        dhead = ListNode(-1, head)
        lastTail = dhead
        cur = dhead.next

        while n >= k:
            tempLastTail = cur
            newHead, cur = self.reverseNNodes(cur, k)
            lastTail.next = newHead
            lastTail = tempLastTail
            n -= k
        
        return dhead.next


