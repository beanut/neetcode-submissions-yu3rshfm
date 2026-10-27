class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        res = [0] * len(heights)

        for i, h in enumerate(heights):
            while stack and stack[-1][0] <= h:
                prev_h, prev_i = stack.pop()
                res[prev_i] += 1
            
            if stack:
                res[stack[-1][1]] += 1
            
            stack.append((h, i))

        return res
        