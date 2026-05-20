class Solution:
    """
    Imagine you have two walls at positions L (left) and R (right). The water they hold is limited by min(height[L], height[R]) × (R - L). The key realization is:

    If you move the taller wall inward, the width shrinks and the effective height can ONLY stay the same or decrease (still capped by the shorter wall). So the area is guaranteed to decrease or stay the same — you can't gain anything.
    If you move the shorter wall inward, yes the width shrinks, but now you have a chance of finding a taller wall that increases the height enough to compensate. You might find a bigger area.

    So the algorithm is: always discard the shorter wall by moving that pointer inward. 
    """
    def maxArea(self, heights: List[int]) -> int:
        curMax = 0

        l = 0
        r = len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            curMax = max(area, curMax)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return curMax