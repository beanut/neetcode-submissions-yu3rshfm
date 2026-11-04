class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0

        zeros = 0
        maxlen = 0
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                l += 1
                if nums[l - 1] == 0:
                    zeros -= 1
            maxlen = max(maxlen, r - l + 1)
            r += 1
        
        return maxlen
