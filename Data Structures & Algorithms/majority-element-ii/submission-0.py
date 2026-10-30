class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        thres = len(nums) // 3
        res = []

        for n, f in counts.items():
            if f > thres:
                res.append(n)

        return res