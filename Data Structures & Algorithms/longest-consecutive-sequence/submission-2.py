class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        curMax = 0

        for n in nums:
            # here we check if n is the start of a consecutive sequence
            # n is the start only if n - 1 is not in nums
            if n - 1 not in store:
                cur = 1

                # if n is the start of a sequence, we count how long the sequence is
                while n + cur in store:
                    cur += 1
                curMax = max(cur, curMax)
        
        return curMax