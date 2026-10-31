class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        1 <= res <= max(piles)
        """

        def hoursNeeded(rate) -> int:
            res = 0
            for p in piles:
                res += -(p // -rate)
            return res
        
        l = 1
        r = max(piles)

        smallest = h
        while l <= r:
            mid = (l + r) // 2
            needed = hoursNeeded(mid)
            if needed <= h:
                smallest = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return smallest