class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        res = hi

        while hi >= lo:
            mid = (hi + lo) // 2

            temph = 0
            for b in piles:
                temph += math.ceil(b / mid)

            if temph <= h:
                hi = mid - 1
                res = mid
            else:
                lo = mid + 1
            
        return res