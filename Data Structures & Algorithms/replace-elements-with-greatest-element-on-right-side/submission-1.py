class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curMax = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            arr[i], curMax = curMax, max(arr[i], curMax)
        return arr