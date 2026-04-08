# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use slow/fast pointer method
        # fast pointer is (n - 1) position(s) ahead of slow
        dummy = ListNode(-1, head)
        fast = head
        for _ in range(n - 1):
            fast = fast.next

        slow = dummy
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        next = slow.next.next
        slow.next = next

        return dummy.next


        