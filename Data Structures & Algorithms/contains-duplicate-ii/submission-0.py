class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = 0
        n = len(nums)

        seen = set([nums[0]])

        while r + 1 < n:
            windowLength = r - l
            if windowLength < k:
                r += 1
                if nums[r] in seen:
                    return True
                seen.add(nums[r])
            else:
                l += 1
                r += 1
                seen.remove(nums[l - 1])
                if nums[r] in seen:
                    return True
                seen.add(nums[r])
            
        return False
            
                