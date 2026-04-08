class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = [0] * 10000

        for n in nums:
            idx = n - 1
            if seen[idx] > 0:
                return n
            else:
                seen[idx] += 1
        
        