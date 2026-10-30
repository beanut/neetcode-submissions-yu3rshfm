class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)
        history = defaultdict(int)
        history[0] += 1
        count = 0

        for i, num in enumerate(nums):
            prefix = num + prefixSum[i]
            prefixSum[i + 1] = prefix
            # existence of prev prefix = prefix - k
            # sum of nums[a:b] = prefixSum[b] - prefixSum[a]
            target = prefix - k
            count += history[target]
            history[prefix] += 1

        return count

        
        