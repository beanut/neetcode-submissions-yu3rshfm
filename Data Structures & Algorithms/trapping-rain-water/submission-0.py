class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        leftMax = height[l]
        rightMax = height[r]

        sum = 0

        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                sum += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                sum += rightMax - height[r]

        return sum
