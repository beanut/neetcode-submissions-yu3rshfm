class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()

        l = 0
        r = 0

        lmax = 0

        while r < len(s):
            while s[r] in track:
                track.remove(s[l])
                l += 1
            
            track.add(s[r])
            r += 1
            lmax = max(lmax, r - l)

        return lmax
