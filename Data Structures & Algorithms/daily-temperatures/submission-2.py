class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = [] # pairs of (t, i)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                diff = i - stack[-1][1]
                out[stack[-1][1]] = diff
                stack.pop()
            stack.append((t, i))
        
        return out