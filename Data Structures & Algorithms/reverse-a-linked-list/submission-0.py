# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseListRecurse(self, prev: Optional[ListNode], node: ListNode):
        temp = node.next
        node.next = prev
        if temp == None:
            return node
        else:
            return self.reverseListRecurse(node, temp)


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        return self.reverseListRecurse(None, head)