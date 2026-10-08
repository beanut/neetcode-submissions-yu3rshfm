class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        # [-4, -1, -1, 0, 1, 2]
        for m in range(len(nums) - 2):
            if m > 0 and nums[m] == nums[m-1]:
                continue

            l = m + 1
            r = len(nums) - 1

            while l < r:
                total = nums[r] + nums[l]

                if total == -nums[m]:
                    res.append([nums[l], nums[m], nums[r]])

                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    
                elif total < -nums[m]:
                    l += 1
                else:
                    r -= 1
        
        return res

