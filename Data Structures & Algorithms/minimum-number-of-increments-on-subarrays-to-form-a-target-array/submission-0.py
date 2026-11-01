class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        count = 0
        prev = 0
        for t in target:
            count += max(t - prev, 0)
            prev = t
        return count
