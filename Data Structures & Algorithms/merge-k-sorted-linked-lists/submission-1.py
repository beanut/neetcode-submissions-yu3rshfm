# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dhead = ListNode(-1)
        cur = dhead

        curheap = []
        while True:
            allNone = True
            for index, head in enumerate(lists):
                if head is not None:
                    allNone = False
                    heapq.heappush(curheap, head.val)
                    lists[index] = head.next
            if allNone:
                break
        
        while curheap:
            newNode = ListNode(heapq.heappop(curheap))
            cur.next = newNode
            cur = cur.next
        
        return dhead.next
