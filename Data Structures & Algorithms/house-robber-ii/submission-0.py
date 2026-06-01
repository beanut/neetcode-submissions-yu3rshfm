class Solution:
    def rob_linear(self, nums: List[int]) -> int:
        prev1, prev0 = 0, 0

        for n in nums:
            prev1, prev0 = prev0, max(prev1 + n, prev0)
        return prev0

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.rob_linear(nums[:-1]), self.rob_linear(nums[1:]))
        