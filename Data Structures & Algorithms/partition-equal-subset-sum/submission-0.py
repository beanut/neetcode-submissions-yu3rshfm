class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        
        if s % 2:
            return False
        
        target = s // 2

        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextdp = dp.copy()
            for t in dp:
                nextdp.add(t + nums[i])
            dp = nextdp
        
        return True if target in dp else False
        