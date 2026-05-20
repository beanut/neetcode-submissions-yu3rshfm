class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        curMax = 0

        for n in nums:
            if n - 1 not in store:
                # n is the start of a sequence
                cur = 1
                while n + cur in store:
                    cur += 1
                curMax = max(curMax, cur)
        
        return curMax
