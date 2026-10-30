class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # started 8:41

        distances = list(map(lambda cur: (abs(x - cur), cur), arr))

        heapq.heapify(distances)

        res = []

        while k > 0:
            cur = heapq.heappop(distances)
            res.append(cur[1])
            k -= 1

        # distances.sort()

        return sorted(res)