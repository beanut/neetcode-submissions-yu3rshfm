class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        curMax = 0
        starts = []

        for n in nums:
            if n - 1 not in store:
                cur = 1
                while n + cur in store:
                    cur += 1
                curMax = max(cur, curMax)
        
        return curMax