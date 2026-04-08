# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is now the middle node
        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        # prev is the head of the reversed list
        first = head
        second = prev
        while second:
            firstNext = first.next
            first.next = second
            secondNext = second.next
            second.next = firstNext
            second = secondNext
            first = firstNext