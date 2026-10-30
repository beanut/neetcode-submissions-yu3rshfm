class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        k = 1
        for i, n in enumerate(nums):
            if i > 0 and n != nums[i - 1]:
                k += 1
                nums[write] = n
                write += 1
        
        return k
            

