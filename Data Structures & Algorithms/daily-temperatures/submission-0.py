class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = [] # stack of [t, i]
        for i, t in enumerate(temperatures):
            while stack and t> stack[-1][0]:
                stackT, stackInd = stack.pop()
                out[stackInd] = i - stackInd
            stack.append((t,i))
        return out
