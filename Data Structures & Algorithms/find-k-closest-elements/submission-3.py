class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # optimal solution with binary search
        # for arr = [2,4,5,8], k = 2, x = 6
        # [4, 2, 1, 2]
        
        l = 0
        r = len(arr) - k

        while l < r:
            mid = (l + r) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        
        return arr[l : l + k]