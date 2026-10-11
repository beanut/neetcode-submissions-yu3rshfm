class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ret = []
        
        def dfs(n: int, path: List[int]):
            if n < 0:
                return
            if n == 0:
                ret.append(path)
                return
            
            for num in nums:
                if path and num < path[-1]: 
                    continue
                
                dfs(n - num, path + [num])
        
        dfs(target, [])
        return ret
        