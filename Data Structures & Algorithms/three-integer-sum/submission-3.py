import copy

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # d = defaultdict(list)
        # for i, x in enumerate(nums):
        #     d[x].append(i) 

        nums.sort()

        c = 0
        while c < len(nums) - 2:
            # only start checking when you're at index 1; no point checking when c == 0
            if c > 0 and nums[c] == nums[c - 1]:
                c += 1
                continue

            l = c + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[l] + nums[r]
                if sum == -nums[c]:
                    res.append([nums[c], nums[l], nums[r]])
                    while l < r and nums[l] == nums [l + 1]:
                        l += 1
                    while l < r and nums[r] == nums [r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sum < -nums[c]:
                    l += 1
                else:
                    r -= 1
             
            c += 1
        return res
            