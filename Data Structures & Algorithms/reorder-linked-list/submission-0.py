# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the second middle
        if not head:
            return None
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the linked list from node at slow to end
        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        # prev is the new head of the reversed linked list
        first = head
        second = prev
        
        while second:
            tempLeft = first.next
            tempRight = second.next
            first.next = second
            second.next = tempLeft
            first = tempLeft
            second = tempRight

