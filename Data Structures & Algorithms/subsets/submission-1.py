class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, cur):
            if start == len(nums):
                res.append(cur[:])
                return 
            # include:
            backtrack(start + 1, cur + [nums[start]])
            # exclude
            backtrack(start + 1, cur)
        
        backtrack(0, [])
        return res
        