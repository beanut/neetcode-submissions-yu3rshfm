from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        store = defaultdict(int)

        maxl = 1

        l = 0
        for i in range(len(s)):
            if s[i] in store and store[s[i]] >= l:
                l = store[s[i]] + 1
            maxl = max(maxl, i - l + 1)
            store[s[i]] = i

        return maxl
            

            