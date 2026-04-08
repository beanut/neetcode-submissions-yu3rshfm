class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        vlo = 0
        vhi = len(matrix) - 1
        vmid = 0

        while vhi >= vlo:
            vmid = vlo + int((vhi - vlo) / 2)
            if matrix[vmid][0] > target:
                vhi = vmid - 1
            elif matrix[vmid][-1] < target:
                vlo = vmid + 1
            else: 
                break
        
        focus = matrix[vmid]
        hlo = 0
        hhi = len(focus) - 1

        while hhi >= hlo:
            hmid = hlo + int((hhi - hlo) / 2)
            if focus[hmid] > target:
                hhi = hmid - 1
            elif focus[hmid] < target:
                hlo = hmid + 1
            else:
                return True

        return False