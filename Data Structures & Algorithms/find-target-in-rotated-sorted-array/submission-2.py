class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while hi > lo:
            mid = (hi + lo) // 2
            if nums[mid] <= nums[hi]:
                hi = mid
            elif nums[mid] > nums[hi]:
                lo = mid + 1
        
        if lo == 0: # not rotated
            hi = len(nums) - 1
        elif target >= nums[0] and target <= nums[lo - 1]:
            hi = lo - 1
            lo = 0
        else:
            hi = len(nums) - 1
    
        while hi >= lo:
            mid = (hi + lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                return mid
        
        return -1