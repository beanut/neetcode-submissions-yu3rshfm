# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2
        carry = 0
        res = ListNode() # starts with dummy node
        cur = res

        while c1 or c2 or not carry == 0:
            n1 = 0 if c1 == None else c1.val
            n2 = 0 if c2 == None else c2.val

            next = ListNode((n1 + n2 + carry) % 10)
            cur.next = next
            cur = cur.next

            carry = (n1 + n2 + carry) // 10

            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next

        return res.next
