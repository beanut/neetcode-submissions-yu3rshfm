class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify_max(heap)

        for _ in range(k-1):
            heapq.heappop_max(heap)

        return heap[0]