class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        LIS = [1] * n

        # Simplifies into a Longest Increasing Subsequence (LIS)

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if envelopes[i][1] < envelopes[j][1]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)