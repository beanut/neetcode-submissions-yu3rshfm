class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        used = [False] * len(nums)
        perm = []

        def dfs():
            if len(perm) == len(nums):
                # use .copy() to make a deepcopy, otherwise it would be a shallow copy (reference)
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                # in-place backtracking solution for memory efficiency
                if not used[i]:
                    used[i] = True
                    perm.append(nums[i])
                    dfs()
                    perm.pop()
                    used[i] = False
                
        dfs()

        return res