class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)

        def dfs(cur: int) -> int:
            if cur < 0:
                return 0
            if cur == 0:
                return 1
            
            if memo[cur] != -1:
                return memo[cur]

            ways = dfs(cur - 1) + dfs(cur - 2)
        
            memo[cur] = ways
            return ways
        
        return dfs(n)