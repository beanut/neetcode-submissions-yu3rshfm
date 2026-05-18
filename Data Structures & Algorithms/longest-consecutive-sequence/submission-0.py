class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        curMax = 0
        starts = []

        for n in nums:
            if n - 1 not in store:
                starts.append(n)
        
        for s in starts:
            cur = 1
            n = s
            while n + 1 in store:
                cur += 1
                n += 1
            curMax = max(curMax, cur) 

        return curMax