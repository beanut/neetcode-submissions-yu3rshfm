from collections import defaultdict

class TimeMap: 

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]
        
        # binary search:
        # Note: the tuples are always sorted by timestamp 
        lo = 0
        hi = len(arr)
        ret = ""

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if arr[mid][0] <= timestamp:
                ret = arr[mid][1]
                lo = mid + 1
            else:
                hi = mid 
        
        return ret