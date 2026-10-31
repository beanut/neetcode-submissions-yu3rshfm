class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0

        seen = defaultdict(int) # char -> freq

        maxf = 0
        maxlen = 0

        # can go forward while curlen - maxf <= k
        while r < len(s):
            c = s[r]
            seen[c] += 1
            maxf = max(maxf, seen[c])
            if r - l + 1 - maxf > k:
                # time to move forward!
                seen[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)
            r += 1
        return maxlen