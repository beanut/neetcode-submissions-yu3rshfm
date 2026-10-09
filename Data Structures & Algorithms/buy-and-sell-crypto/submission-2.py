class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        prof = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                prof = max(prof, prices[r] - prices[l])
            
            r += 1
        
        return prof
