class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix)

        while t < b:
            mid = (t + b) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                # perform binary search on that row
                l = 0
                r = len(matrix[0])
                while l < r:
                    rowmid = (l + r) // 2
                    if matrix[mid][rowmid] == target:
                        return True
                    elif target < matrix[mid][rowmid]:
                        r = rowmid
                    else:
                        l = rowmid + 1
                print("hmm")
                return False
            elif target < matrix[mid][0]:
                b = mid
            else:
                t = mid + 1
        
        return False