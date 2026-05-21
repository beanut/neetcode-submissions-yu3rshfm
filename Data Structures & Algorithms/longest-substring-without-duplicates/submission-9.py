class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         if not s:
            return 0

         seen = defaultdict(int)

         l = 0
         r = 0

         res = 1

         while r < len(s):
            if s[r] in seen and l <= seen[s[r]]:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
                

         return res
