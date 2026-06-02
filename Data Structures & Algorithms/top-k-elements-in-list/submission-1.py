from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = [[] for _ in range(len(nums) + 1)] # f[i] returns list of nums that occur i times

        count = Counter(nums)

        for key, v in count.items():
            f[v].append(key)

        res = []
        for i in range(len(f) - 1, 0, -1):
            for num in f[i]:
                res.append(num)
                if len(res) == k:
                    return res


