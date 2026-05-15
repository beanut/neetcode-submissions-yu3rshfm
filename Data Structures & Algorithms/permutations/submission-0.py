class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(perm: List[int], used: List[bool]):
            if len(perm) == len(nums):
                res.append(perm)
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    newUsed = used.copy()
                    newUsed[i] = True
                    dfs(perm + [nums[i]], newUsed)
                
        dfs([], [False] * len(nums))

        return res