class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev = 0, 0
        for n in nums:
            prev2, prev = prev, max(prev, prev2 + n)
        return prev