import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)

        maxheap = []

        for p in points:
            dist = (p[0] ** 2 + p[1] ** 2)
            heapq.heappush_max(maxheap, [dist, p])
            if len(maxheap) == k + 1:
                heapq.heappop_max(maxheap)
        
        return list(map(lambda x : x[1], maxheap))

