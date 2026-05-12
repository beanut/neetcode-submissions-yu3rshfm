class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # a heap of tuples (distance: int, point: List[int])
        heap = []

        # precompute distances
        for point in points:
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)

            heap.append((distance, point))
            
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            cur = heapq.heappop(heap)
            res.append(cur[1])
        
        return res
