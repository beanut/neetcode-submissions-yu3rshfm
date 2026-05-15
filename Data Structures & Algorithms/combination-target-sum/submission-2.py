class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        # we sort nums and enforce an order in recursion
        def dfs(curMinIdx: int, sum: int, cur: List[int]):
            if sum >= target:
                if sum == target:
                    res.append(cur)
                return
            
            for i in range(curMinIdx, len(nums)):
                dfs(i, sum + nums[i], cur + [nums[i]])
        
        dfs(0, 0, [])
        return res
