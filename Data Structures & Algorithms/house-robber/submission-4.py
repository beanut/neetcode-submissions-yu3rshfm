class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        at any house:
        if rob:
            can only rob again starting i + 2
        if not robbing:
            can rob at i + 1
        """

        dp = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))

            return dp[i]

        return dfs(0)

