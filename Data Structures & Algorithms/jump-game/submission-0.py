class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dead = set()

        def dfs(idx) -> bool:
            if idx == len(nums) - 1:
                return True
            if idx in dead:
                return False
            
            for nxt in range(idx + 1, idx + nums[idx] + 1):
                if dfs(nxt):
                    return True
            
            dead.add(idx)
            return False

        return dfs(0)