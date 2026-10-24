class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 3:37
        # dp[p][q] = # of ways at node q at level p
        # dp = [[-1] * (target + 1) for _ in range(len(nums))]
        dp = defaultdict(lambda: [-1] * len(nums))

        def dfs(r: int, start: int) -> int:
            if start == len(nums) and r == 0:
                return 1
            if start >= len(nums):
                return 0
            if r in dp and dp[r][start] > -1:
                return dp[r][start]

            cur = nums[start]
            dp[r][start] = dfs(r - cur, start + 1) + dfs(r + cur, start + 1)
            return dp[r][start]

        return dfs(target, 0)

            