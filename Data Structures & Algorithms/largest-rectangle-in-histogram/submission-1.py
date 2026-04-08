class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # monotonic non decreasing; pairs of (i, h)
        curMax = 0

        for i, h in enumerate(heights):
            lastI = i
            while stack and stack[-1][1] > h:
                lastIdx, lastH = stack[-1]
                # calculate max area of the rect bout to be popped:
                area = (i - lastIdx) * lastH
                curMax = max(area, curMax)
                stack.pop()
                lastI = lastIdx
            stack.append((lastI, h))

        # calc the area of the remaining rects:
        for i, h in stack:
            curMax = max(curMax, (len(heights) - i) * h)
        
        return curMax
                



        
