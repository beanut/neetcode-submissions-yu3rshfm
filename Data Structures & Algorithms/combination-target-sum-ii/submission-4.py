class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(path: List[int], s: int, start: int):
            if s == target:
                res.append(path)
                return
            elif s > target:
                return
            
            for i in range(start, len(candidates)):
                if i - 1 >= start and candidates[i] == candidates[i - 1]:
                    continue
                c = candidates[i]
                backtrack(path + [c], s + c, i + 1)


        backtrack([], 0, 0)    
        return res
