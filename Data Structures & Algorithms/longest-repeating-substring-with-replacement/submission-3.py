class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0

        maxlen = 0

        maxf = 0
        store = defaultdict(int) # store the freq of the chars in the current window

        # formula: len(window) - maxf <= k
        while r < len(s):
            store[s[r]] += 1
            maxf = max(maxf, store[s[r]])
            if (r - l + 1) - maxf > k:
                store[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)
            r += 1
                
            
        return maxlen

        