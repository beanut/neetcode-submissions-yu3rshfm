class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(idx: int, cur: List[int]):
            if idx == len(nums):
                res.append(cur)
                return
            # include:
            dfs(idx + 1, cur + [nums[idx]])
            # exclude
            dfs(idx + 1, cur)

        dfs(0, [])
        return res