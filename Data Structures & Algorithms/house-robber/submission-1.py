class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        cache = [-1] * len(nums)

        cache[0] = nums[0]
        cache[1] = max(nums[1], nums[0])

        r = 2
        loot = 0

        while r < len(nums):
            cache[r] = max(cache[r - 2] + nums[r], cache[r - 1])
            r += 1

        return cache[-1]

