class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curMax = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            curArea = min(heights[l], heights[r]) * (r-l)
            curMax = max(curMax, curArea)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return curMax