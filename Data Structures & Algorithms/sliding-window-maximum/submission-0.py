class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for r in range(len(nums)):
            heapq.heappush_max(heap, (nums[r], r))
            if r - k >= -1:
                while heap[0][1] < r - k + 1:
                    heapq.heappop_max(heap)
                res.append(heap[0][0])
        return res