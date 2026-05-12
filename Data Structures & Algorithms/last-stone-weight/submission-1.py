class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)

        while len(heap) > 1:
            prevMax = heapq.heappop_max(heap)
            nextMax = heapq.heappop_max(heap)

            if prevMax != nextMax:
                heapq.heappush_max(heap, abs(prevMax - nextMax))
            
        if not heap:
            return 0
        else:
            return heap[0]
            