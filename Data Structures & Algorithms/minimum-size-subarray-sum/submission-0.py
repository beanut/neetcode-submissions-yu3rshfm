class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)

        for i, n in enumerate(nums):
            prefix[i + 1] = n + prefix[i]

        smallest = float("inf")
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) + 1

            while l < r:
                mid = (r + l) // 2
                if prefix[mid] - prefix[i] < target:
                    l = mid + 1
                else:
                    r = mid
            
            if l <= len(nums):
                smallest = min(smallest, l - i)
        
        return 0 if smallest == float("inf") else smallest

