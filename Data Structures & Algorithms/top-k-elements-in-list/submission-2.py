class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]

        c = Counter(nums)

        for key, value in c.items():
            bucket[value].append(key)
        
        res = []

        for r in range(len(nums), 0, -1):
            for n in bucket[r]:
                res.append(n)
                if (len(res) == k):
                    return res
