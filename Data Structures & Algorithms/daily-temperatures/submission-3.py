class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pairs of (i, t)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                idiff = i - stack[-1][0]
                res[stack[-1][0]] = idiff
                stack.pop()
            stack.append((i, t))
        
        return res