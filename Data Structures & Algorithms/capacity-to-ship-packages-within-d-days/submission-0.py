class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysNeeded(capacity):
            res = 0
            curLoad = 0

            for w in weights:
                if curLoad + w > capacity:
                    # ship it
                    res += 1
                    curLoad = 0
                curLoad += w
            
            return res if curLoad == 0 else res + 1

        lo = max(weights)
        hi = sum(weights)
        cap = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            need = daysNeeded(mid)
            if need <= days:
                hi = mid - 1
                cap = mid
            else:
                lo = mid + 1
        
        return cap
            