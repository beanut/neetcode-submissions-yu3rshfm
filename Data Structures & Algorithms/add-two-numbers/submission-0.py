# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curOne = l1
        curTwo = l2

        carry = 0

        dummyHead = ListNode(-1)
        dummyCur = dummyHead

        while curOne or curTwo:
            one = 0
            two = 0

            if curOne:
                one = curOne.val
            
            if curTwo:
                two = curTwo.val
            
            sum = (one + two + carry) % 10
            carry = (one + two + carry) // 10

            next = ListNode(sum)
            dummyCur.next = next
            dummyCur = dummyCur.next

            if curOne:
                curOne = curOne.next

            if curTwo:
                curTwo = curTwo.next

        while carry:
            cur = carry % 10

            next = ListNode(cur)

            dummyCur.next = next
            dummyCur = dummyCur.next

            carry = carry // 10

        return dummyHead.next


            