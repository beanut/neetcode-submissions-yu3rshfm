class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = float("inf")

        n = len(cost)
        dp = [-1] * n

        def dfs(start) -> int:
            if start >= n:
                return 0
            
            if dp[start] != -1:
                return dp[start]
            
            cur = cost[start] + min(dfs(start + 1), dfs(start + 2))

            dp[start] = cur

            return cur
        
        dfs(0)
        return min(
            dp[0],
            dp[1]
        )