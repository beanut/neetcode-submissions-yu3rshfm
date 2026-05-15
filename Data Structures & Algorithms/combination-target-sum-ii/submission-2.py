class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        comb = []
        sum = 0

        def dfs(start: int):
            # its best practice to not use a built-in/already-defined symbol
            # in this case, sum()
            nonlocal sum
            if sum >= target:
                if sum == target:
                    res.append(comb[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                sum += candidates[i]

                dfs(i + 1)

                sum -= candidates[i]
                comb.pop()

        dfs(0)
        return res