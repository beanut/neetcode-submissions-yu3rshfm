class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        lmax = height[l]
        rmax = height[r]

        water = 0

        while l < r:
            if height[l] < height[r]:
                lmax = max(lmax, height[l])
                water += lmax - height[l]
                l += 1
            else:
                rmax = max(rmax, height[r])
                water += rmax - height[r]
                r -= 1
        
        return water