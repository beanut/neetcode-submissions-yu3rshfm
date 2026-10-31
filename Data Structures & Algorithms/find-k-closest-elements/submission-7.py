class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = list(map(lambda n: n - x, arr))
        print(diff)
        l = 0
        r = 0
        
        s = 0
        
        while r < k:
            s += abs(diff[r])
            if r == k - 1:
                break
            r += 1
        curMin = s
        ran = [l, r]

        while r < len(arr) - 1:
            r += 1
            s += abs(diff[r])
            s -= abs(diff[l])
            l += 1
            if s < curMin:
                ran = [l, r]
                curMin = s
        
        return arr[ran[0]:ran[1] + 1]


            
