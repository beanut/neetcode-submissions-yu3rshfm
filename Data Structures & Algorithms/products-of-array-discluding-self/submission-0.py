class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltr = [1]
        rtl = [1]

        for n in nums[:-1]:
            ltr.append(ltr[-1] * n)

        for n in reversed(nums[1:]):
            rtl.append(rtl[-1] * n)
        
        rtl.reverse()

        return [l * r for r,l in zip(ltr, rtl)]

