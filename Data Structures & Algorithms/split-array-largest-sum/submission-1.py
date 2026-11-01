class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        [min(nums), sum(nums)]
        """

        def kNeeded(maxPerPart) -> int:
            count = 0
            curSum = 0
            for n in nums:
                if curSum + n > maxPerPart:
                    count += 1
                    curSum = 0
                curSum += n
            return count if curSum == 0 else count + 1

        lo = max(nums) 
        hi = sum(nums)

        while lo <= hi:
            mid = (lo + hi) // 2
            needed = kNeeded(mid)
            if needed <= k:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return lo
