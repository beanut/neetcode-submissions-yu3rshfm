class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        10, 8, 9
        10, 9
        """
        stack = []
        res = [0] * len(heights)

        for i, h in enumerate(heights):
            while stack and stack[-1][1] <= h:
                prev_i, prev_h = stack.pop()
                res[prev_i] += 1
            
            if stack:
                res[stack[-1][0]] += 1
            
            stack.append((i, h))

        return res

        


