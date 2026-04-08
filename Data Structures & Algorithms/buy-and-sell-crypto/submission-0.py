class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1

        pmax = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                pmax = max(pmax, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1
        
        return pmax
